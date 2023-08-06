import datetime
import pandas as pd
import numpy as np
import LibHanger.Library.uwLogger as Logger
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
from stockgetter2.Models.mstBrand import mstbrand
from stockgetter2.Models.trnDayStockPrice import trnDayStockPrice
from stockgetter2.Getter.Base.baseGetter import baseGetter

class getter_seleniumTest(baseGetter):
    
    """
    Selenium実行テストクラス
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

    def init_recset(self):
        """
        レコードセット初期化
        """

        # レコードセット初期化
        self.rsTrnDayStockPrice = recset[trnDayStockPrice](trnDayStockPrice)

    @Logger.loggerDecorator("getData")
    def getData(self, rsMstBrand:recset[mstbrand], *args, **kwargs):
        
        """
        株価データ取得
        
        Parameters
        ----------
        kwargs : str
            @brandCd
                銘柄コード
        """
        
        result = None
        try:
            kwargs['getter'] = self
            
            # 株価データ取得
            rsMstBrand.first()
            while rsMstBrand.eof() == False:
                Logger.logging.info('>>>>>> Started Get TrnDayStockPrice Target brandcd={0}.'.format(rsMstBrand.fields(mstbrand.brandcd.key).value))
                kwargs['brandCd'] = rsMstBrand.fields(mstbrand.brandcd.key).value
                df = self.getStockDataToDataFrame(**kwargs)
                Logger.logging.info('<<<<<< Finished Get TrnDayStockPrice Count={0}.'.format(len(df) if not df is None else 0))
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

        # ウィンドウサイズを1200x1000にする
        self.wdc.browserCtl.changeBrowserSize('1200', '1000')
        
        # ページロード
        self.wdc.browserCtl.loadPage(stockDataUrl)
        
        # pandasデータを返却する
        return self.wdc.browserCtl.createSearchResultDataFrame(**kwargs)

    class chrome(browserContainer.chrome):
        
        """
        ブラウザコンテナ:chrome
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
            
            #print('element_count={}'.format(len(element)))
            
            # getterインスタンス取得
            bc:getter_seleniumTest = kwargs.get('getter')

            # 銘柄コード取得
            brandCd = kwargs.get('brandCd')
            print(brandCd)
            
            # html解析
            #html = self.wDriver.page_source.encode('utf-8')
            #html = element[0].parent.page_source
            html = element.parent.page_source
            bsSrc = BeautifulSoup(html, 'lxml')
            
            # スクレイピング結果から改行ｺｰﾄﾞを除去
            [tag.extract() for tag in bsSrc(string='\n')]

            # 株価データ取得
            rankingTables = bsSrc.find_all(class_="rankingFrame")
            
            # 株価データmodel用意
            rsTrnDayStockPrice = recset[trnDayStockPrice](trnDayStockPrice)

            if rankingTables:
                
                print('Data Exists.')
                
                # 戻り値を返す
                df = rsTrnDayStockPrice.getDataFrame()
                print('brandcd={} count={}'.format(brandCd,len(df)))
                return df
            else:
                print('brandcd={}'.format(brandCd))
                print('Data Not Exists.')

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
            