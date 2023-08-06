import datetime
import pandas as pd
import numpy as np
import gc
import requests
import LibHanger.Library.uwLogger as Logger
import LibHanger.Library.uwGetter as Getter
from bs4 import BeautifulSoup
from pandas.core.frame import DataFrame
from enum import Enum
from decimal import Decimal
from LibHanger.Models.recset import recset
from Scrapinger.Library.browserContainer import browserContainer
from stockgetter2.Library.stockgetterConfig import stockgetterConfig
from stockgetter2.Library.stockgetterGlobals import *
from stockgetter2.Library.stockgetterException import getterError
from stockgetter2.Library.stockgetterException import gettingValueError
from stockgetter2.Models.trnDayStockPrice import trnDayStockPrice
from stockgetter2.Getter.Base.baseGetter import baseGetter

class getter_trnDayStockPrice(baseGetter):
    
    """
    株価データ取得クラス
    (trndaystockprice)
    """

    def __init__(self) -> None:
        
        """
        コンストラクタ
        """
        
        super().__init__()

        # レコードセット初期化
        self.init_recset()

        # スクレイピング準備
        self.wdc.settingScrape()

        # 取込対象リストの列定義
        #['', '順位',	'コード', '名称', '市場' , '日付' , '取引値', '前日比(円)', '前日比(%)', '出来高', '高値', '安値']
        self.targetListCols = ['', 'No',	'StockCode', 'StockName', 'Market' , 'Date' , 'Close', 'BeforeRetio', 'BeforeRetioPer', 'Volume', 'High', 'Low']
    
    def init_recset(self):
        """
        レコードセット初期化
        """

        # レコードセット初期化
        self.rsTrnDayStockPrice = recset[trnDayStockPrice](trnDayStockPrice)

    @Logger.loggerDecorator("getTargetMstBrand")
    def getTargetMstBrand(self):
        
        """
        対象銘柄マスタ取得
        """

        # スクレイピングで取得可能な日付を取得
        bs = None
        for offSet in range(-1, -10, -1):
            
            # 前日か前々日のランキング取得
            targetOffSet = offSet
            bs = self.getBsTarget(targetOffSet, 0)
            if bs != None : break
        
        # 取得失敗時は処理を終了
        if bs == None :
            msg = 'Get TargetDate Failed.'
            print(msg)
            Logger.logging.error(msg)
            return None

        # ページインデックスをループして対象銘柄取得(0～10で固定。9,10は存在しない為、取得失敗想定)
        dfMain = self.getTargetListDataFrame(bs)
        for pageIdx in range(0, 10):

            # 対象銘柄をスクレイピングで取得
            bs = self.getBsTarget(targetOffSet, pageIdx)
            if bs == None : continue
            # 対象銘柄リスト取得    
            df = self.getTargetListDataFrame(bs)

            # DataFrame結合
            dfMain = pd.concat([dfMain, df],axis=0)

        # [取引値]列をint32に変換して取得
        col_Close = dfMain['Close']
        col_Close = col_Close.astype('float32').round().astype('int32')
        
        # 取引値範囲で絞り込み
        rowCount = dfMain.shape[0]
        if rowCount == 0:
            msg = 'Get TargetDataFrame Failed.'
            print(msg)
            Logger.logging.error(msg)
            return None
        
        dfMain = dfMain[(col_Close >= int(gv.stockgetterConfig.closeFrom)) & (col_Close <= int(gv.stockgetterConfig.closeTo))]

        # 絞り込み結果をDataFrameに変換
        return pd.DataFrame(dfMain, columns = self.targetListCols)
    
    def getBsTarget(self, curDateOffset, pageIndex):

        """ 
        スクレイピングにより取得したBeautifulSoup オブジェクトを取得する
        
        Parameters
        ----------
        curDateOffset :
            現在日付から過去日付に向かってシフトする日数
        pageIndex :
            対象サイトのページインデックス
        """

        # 現在日付の前日取得
        curDate = Getter.addDays(Getter.getNow(), curDateOffset).strftime('%Y/%m/%d')
        
        # 対象URL
        url = gv.stockgetterConfig.kabuDragonTeiiUrl.format(curDate, '' if pageIndex == 0 else str(pageIndex))

        # レスポンスの lxml から BeautifulSoup オブジェクトを生成
        bs = BeautifulSoup(requests.get(url).text, "lxml")

        # 取得結果判定
        return bs if len(bs.body.find_all('tr')) > 20 else None
    
    def getTargetListDataFrame(self, bs):

        """ 
        株価データ取得対象となる銘柄コードリストをDataFrameで取得する
        
        Parameters
        ----------
        bs :
            BeautifulSoup オブジェクト
        """

        start_line = [i for i in range(7,20) if bs.body.find_all('tr')[i].text.splitlines()[1] == '順位']
        items = [v.text.splitlines() for i, v in enumerate(bs.body.find_all('tr')) if i > start_line[0]]
        df = pd.DataFrame(np.array(items[0]).reshape(1,-1),columns=self.targetListCols)
        for i in range(1,50):
            df_add = pd.DataFrame(np.array(items[i]).reshape(1,-1),columns=self.targetListCols)
            df = pd.concat([df, df_add],axis = 0)

        return df
    
    @Logger.loggerDecorator("getData")
    def getData(self, *args, **kwargs):
        
        """
        株価データ取得
        
        Parameters
        ----------
        rsMstBrand : recset[mstbrand]
            対象となる銘柄マスタ
        kwargs : str
            @brandCd
                銘柄コード
        """
        
        result = None
        try:
            kwargs['getter'] = self
            
            # 対象銘柄DataFrame取得
            dfTargetBrand = self.getTargetMstBrand()
            # 株価データ取得
            for index, item in dfTargetBrand.iterrows():
                brandCd = item['StockCode']
                Logger.logging.info('>>>>>> Started Get TrnDayStockPrice Target brandcd={0}.'.format(brandCd))
                kwargs['brandCd'] = brandCd
                df = self.getStockDataToDataFrame(**kwargs)
                Logger.logging.info('<<<<<< Finished Get TrnDayStockPrice Count={0}.'.format(len(df)))
                del df
                gc.collect()
                # mem-check
                self.cbCheckMem()
            
        except Exception as e: # その他例外
            Logger.logging.error(str(e))
            raise getterError
        
        return result
    
    def cbCheckMem():
        pass
    
    @Logger.loggerDecorator("getStockDataToDataFrame")
    def getStockDataToDataFrame(self, *args, **kwargs):

        """
        株価データ取得
        
        Parameters
        ----------
        kwargs : str
            @brandCd
                銘柄コード
        """
        
        # 検索url(ルート)
        rootUrl = gv.stockgetterConfig.kabuDragonUrl
        # 検索url(銘柄情報)
        stockDataUrl = rootUrl.format(kwargs.get('brandCd'))
        
        # ページロード
        self.wdc.browserCtl.loadPage(stockDataUrl)
        
        # pandasデータを返却する
        return self.wdc.browserCtl.createSearchResultDataFrame(**kwargs)
    
    def getPrice(self, priceString:str):
        
        """
        株価取得
        
        Parameters
        ----------
        priceString : str
            株価(文字列)
        """
        
        stockPrice = 0
        
        try:
            # 株価文字列を数値に変換
            stockPrice_str = priceString.replace(',','')
            try:
                stockPrice = Decimal(stockPrice_str.replace(',',''))
            except ValueError as e:
                raise
            
        except Exception as e:
            Logger.logging.error('stock_price Get Error : Value=' + stockPrice_str)
            Logger.logging.error(str(e))
            raise gettingValueError
            
        return stockPrice
    
    def getSma(self, priceList:DataFrame, smaSpan):

        """
        単純移動平均(SMA)計算 
        """

        return priceList.rolling(smaSpan).mean()

    def getEma(self, priceList:DataFrame, emaSpan):

        """
        平滑指数移動平均(EMA)計算 
        """
        
        s = pd.Series(priceList)
        sma = s.rolling(emaSpan).mean()[:emaSpan]
        return pd.concat([sma, s[emaSpan:]]).ewm(span=emaSpan,adjust=False).mean()

    def getRSI(self, priceList:DataFrame, rsiSpan):

        """
        RSI計算 
        """

        # 終値の差分取得
        diff = priceList.diff()
        diff = diff[1:]

        # 値上がり幅/値下がり幅をシリーズへ切り分け
        up, down = diff.copy(), diff.copy()
        up[up < 0] = 0
        down[down > 0] = 0
        
        up_sma= up.rolling(rsiSpan, center=False).mean()
        down_sma = down.abs().rolling(rsiSpan, center=False).mean()

        # RS計算
        rs = up_sma / down_sma
        # RSI計算
        rsi = 100.0 - (100.0 / (1.0 + rs))

        return rsi

    def get_buy_signals_macd(self, macd, macdsig):

        """
        MACDのGCによる買いシグナルの取得 
        """

        # 交差点を捕捉
        cross = macd > macdsig
        golden = np.array((cross != np.roll(cross,1)) & (cross == True))

        # 買いシグナルを文字列に置換
        golden = ['買' if value==True else '' for value in golden]

        # 買いシグナルの結果を返す
        return golden

    def get_sell_signals_macd(self, macd, macdsig):
        """ 
        MACDのDCによる売りシグナルの取得 
        """

        # 交差点を捕捉
        cross = macd < macdsig
        dead = np.array((cross != np.roll(cross,1)) & (cross == True))

        # 売りシグナルを文字列に置換
        dead = ['売' if value==True else '' for value in dead]

        # 売りシグナルの結果を返す
        return dead

    def get_buy_signals_rsi(self, rsi, rsi_thresold):
        """ 
        RSIによる買いシグナルの取得 
        """

        # rsi買いシグナル捕捉
        buy_signals = np.array((rsi < rsi_thresold) & (rsi != 0))

        # 買いシグナルを文字列に置換
        buy_signals = ['買' if value==True else '' for value in buy_signals]

        # 買いシグナルの結果を返す
        return buy_signals

    def get_sell_signals_rsi(self, rsi, rsi_thresold):
        
        """
        RSIによる売りシグナルの取得 
        """

        # rsi買いシグナル捕捉
        sell_signals = np.array((rsi > rsi_thresold) & (rsi != 100))

        # 売りシグナルを文字列に置換
        sell_signals = ['売' if value==True else '' for value in sell_signals]

        # 売りシグナルの結果を返す
        return sell_signals

    def getMacdSign(self, macdBuy, macdSell):

        """
        MACDサイン取得 
        """

        macdSign = ''

        if macdBuy != '':
            macdSign = macdBuy
        elif macdSell != '':
            macdSign = macdSell
        else:
            macdSign = ''

        return macdSign

    def getRsiSign(self, rsiBuy, rsiSell):

        """
        RSIサイン取得 
        """

        rsiSign = ''

        if rsiBuy != '':
            rsiSign = rsiBuy
        elif rsiSell != '':
            rsiSign = rsiSell
        else:
            rsiSign = ''

        return rsiSign

    class chrome(browserContainer.chrome):
        
        """
        ブラウザコンテナ:chrome
        """

        class stockListCol(Enum):
            
            """
            株価データ列インデックス
            """
            
            stockymd = 0
            """ 日付 """
            
            open = 1
            """ 始値 """

            high = 2
            """ 高値 """

            low = 3
            """ 安値 """

            close = 4
            """ 終値 """

            volume = 6
            """ 出来高 """
            
        def __init__(self, _config: stockgetterConfig):
            
            """
            コンストラクタ
            
            Parameters
            ----------
                _config : stockgetterConfig
                    共通設定
            """
            
            super().__init__(_config)

            self.config = _config
            self.cbCreateSearchResultDataFrameByWebDriver = self.createSearchResultDataFrameByWebDriver

        def createSearchResultDataFrameByWebDriver(self, element, *args, **kwargs) -> DataFrame:
            
            """
            株価情報をDataFrameで返す(By Selenium)
            """
            
            return self.getStockData(element, *args, **kwargs)

        def getStockData(self, element, *args, **kwargs):
            
            """
            株価データをDataFrameで返す(By Selenium)
            
            Parameters
            ----------
            kwargs : str
                @brandCd
                    銘柄コード
            """
            
            # getterインスタンス取得
            bc:getter_trnDayStockPrice = kwargs.get('getter')

            # 銘柄コード取得
            brandCd = kwargs.get('brandCd')
            
            # html解析
            html = element.parent.page_source
            bsSrc = BeautifulSoup(html, 'lxml')

            # スクレイピング結果から改行ｺｰﾄﾞを除去
            [tag.extract() for tag in bsSrc(string='\n')]

            # 株価データ取得
            rankingTables = bsSrc.find_all(class_="rankingFrame")
            
            # 株価データmodel用意
            rsTrnDayStockPrice = recset[trnDayStockPrice](trnDayStockPrice)

            if rankingTables:
                
                rankingTable = rankingTables[1]

                # 株価テーブル取得
                stockList = rankingTable.find_all('tr')
                for stockListRow in stockList:
                    try:
                        # 取得対象行か判定
                        trClass = stockListRow.get('class')
                        if trClass:
                            if trClass[0] == 'evenRow' or trClass[0] == 'oddRow':
                                
                                # 株価情報の行取得
                                drow = stockListRow.contents

                                # 日付
                                stockymd_str = drow[self.stockListCol.stockymd.value].text
                                stockymd = datetime.datetime.strptime(stockymd_str, '%Y/%m/%d')
                                # 始値
                                open = bc.getPrice(drow[self.stockListCol.open.value].text)
                                # 高値
                                high = bc.getPrice(drow[self.stockListCol.high.value].text)
                                # 安値
                                low = bc.getPrice(drow[self.stockListCol.low.value].text)
                                # 終値
                                close = bc.getPrice(drow[self.stockListCol.close.value].text)
                                # 出来高
                                volume = bc.getPrice(drow[self.stockListCol.volume.value].text)

                                # Modelに追加
                                rsTrnDayStockPrice.newRow()
                                rsTrnDayStockPrice.fields(trnDayStockPrice.brandcd.key).value = brandCd
                                rsTrnDayStockPrice.fields(trnDayStockPrice.stockymd.key).value = stockymd
                                rsTrnDayStockPrice.fields(trnDayStockPrice.open.key).value = open
                                rsTrnDayStockPrice.fields(trnDayStockPrice.high.key).value = high
                                rsTrnDayStockPrice.fields(trnDayStockPrice.low.key).value = low
                                rsTrnDayStockPrice.fields(trnDayStockPrice.close.key).value = close
                                rsTrnDayStockPrice.fields(trnDayStockPrice.volume.key).value = volume
                                rsTrnDayStockPrice.fields(trnDayStockPrice.updinfo.key).value = bc.getUpdInfo()
                                
                    except gettingValueError as gvException: # 株価変換例外
                        Logger.logging.error(str(gvException))
                        raise 
                    except Exception as e: # その他例外
                        Logger.logging.error(str(e))
                        raise 
                        
                # DataFrameに変換
                dfTrnDayStockPrice = rsTrnDayStockPrice.getDataFrame()
                # 日付順にソート
                dfTrnDayStockPrice = dfTrnDayStockPrice.set_index([trnDayStockPrice.brandcd.key,trnDayStockPrice.stockymd.key], drop=False)
                dfTrnDayStockPrice = dfTrnDayStockPrice.sort_index()
                
                # 終値取得
                price = dfTrnDayStockPrice[trnDayStockPrice.close.key]
                # 短期sma計算
                dfTrnDayStockPrice[trnDayStockPrice.smashort.key] = bc.getSma(price, gv.stockgetterConfig.smaSpanShort)
                # 中期sma計算
                dfTrnDayStockPrice[trnDayStockPrice.smamidium.key] = bc.getSma(price, gv.stockgetterConfig.smaSpanMidium)
                # 中長期sma計算
                dfTrnDayStockPrice[trnDayStockPrice.smamidiumlong.key] = bc.getSma(price, gv.stockgetterConfig.smaSpanMidiumLong)
                # 短期ema計算
                dfTrnDayStockPrice[trnDayStockPrice.emashort.key] = bc.getEma(price, gv.stockgetterConfig.emaSpanShort)
                # 長期ema計算
                dfTrnDayStockPrice[trnDayStockPrice.emalong.key] = bc.getEma(price, gv.stockgetterConfig.emaSpanLong)
                # MACD計算
                dfTrnDayStockPrice[trnDayStockPrice.macd.key] = bc.getEma(price, gv.stockgetterConfig.emaSpanShort) - bc.getEma(price, gv.stockgetterConfig.emaSpanLong)
                # MACDシグナル計算
                dfTrnDayStockPrice[trnDayStockPrice.macdsig.key] = bc.getEma(dfTrnDayStockPrice[trnDayStockPrice.macd.key], gv.stockgetterConfig.macdSig)
                # RSI計算
                dfTrnDayStockPrice[trnDayStockPrice.rsi.key] = bc.getRSI(price, gv.stockgetterConfig.rsiSpan)
                # MACD買いシグナル
                dfTrnDayStockPrice['macdbuy'] = bc.get_buy_signals_macd(dfTrnDayStockPrice[trnDayStockPrice.macd.key], dfTrnDayStockPrice[trnDayStockPrice.macdsig.key])
                # MACD売りシグナル
                dfTrnDayStockPrice['macdsell'] = bc.get_sell_signals_macd(dfTrnDayStockPrice[trnDayStockPrice.macd.key], dfTrnDayStockPrice[trnDayStockPrice.macdsig.key])
                # RSI買いシグナル
                dfTrnDayStockPrice['rsibuy'] = bc.get_buy_signals_rsi(dfTrnDayStockPrice[trnDayStockPrice.rsi.key], gv.stockgetterConfig.rsiThresoldUnder)
                # RSI売りシグナル
                dfTrnDayStockPrice['rsisell'] = bc.get_sell_signals_rsi(dfTrnDayStockPrice[trnDayStockPrice.rsi.key], gv.stockgetterConfig.rsiThresoldOver)
                
                # 欠損値を0に変換
                dfTrnDayStockPrice = dfTrnDayStockPrice.fillna(0)
                
                # 計算した値をレコードセット側に反映
                rsTrnDayStockPrice.first()
                while rsTrnDayStockPrice.eof() == False:
                    try:
                        df = dfTrnDayStockPrice[
                            (dfTrnDayStockPrice[trnDayStockPrice.brandcd.key] == rsTrnDayStockPrice.fields(trnDayStockPrice.brandcd.key).value) & 
                            (dfTrnDayStockPrice[trnDayStockPrice.stockymd.key] == rsTrnDayStockPrice.fields(trnDayStockPrice.stockymd.key).value)]
                        rsTrnDayStockPrice.editRow()
                        rsTrnDayStockPrice.fields(trnDayStockPrice.smashort.key).value = df.iloc[0][trnDayStockPrice.smashort.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.smamidium.key).value = df.iloc[0][trnDayStockPrice.smamidium.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.smamidiumlong.key).value = df.iloc[0][trnDayStockPrice.smamidiumlong.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.emashort.key).value = df.iloc[0][trnDayStockPrice.emashort.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.emalong.key).value = df.iloc[0][trnDayStockPrice.emalong.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.macd.key).value = df.iloc[0][trnDayStockPrice.macd.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.macdsig.key).value = df.iloc[0][trnDayStockPrice.macdsig.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.rsi.key).value = df.iloc[0][trnDayStockPrice.rsi.key]
                        rsTrnDayStockPrice.fields(trnDayStockPrice.macdsign.key).value = bc.getMacdSign(df.iloc[0]['macdbuy'], df.iloc[0]['macdsell'])
                        rsTrnDayStockPrice.fields(trnDayStockPrice.rsisign.key).value = bc.getRsiSign(df.iloc[0]['rsibuy'], df.iloc[0]['rsisell'])
                    except Exception as e: # その他例外
                        Logger.logging.error(str(e))
                        raise

                # レコードセットマージ
                bc.rsTrnDayStockPrice.merge(rsTrnDayStockPrice, False)
                
                # 使い終わったレコードセットを解放
                del dfTrnDayStockPrice
                
            # 戻り値を返す
            return rsTrnDayStockPrice.getDataFrame()

    class beautifulSoup(browserContainer.beautifulSoup):
        
        """
        ブラウザコンテナ:beautifulSoup
        """

        def __init__(self, _config: stockgetterConfig):
            
            """
            コンストラクタ
            
            Parameters
            ----------
                _config : stockgetterConfig
                    共通設定
            """

            super().__init__(_config)
            
            self.config = _config
            self.cbCreateSearchResultDataFrameByBeutifulSoup = self.createSearchResultDataFrameByBeutifulSoup
            