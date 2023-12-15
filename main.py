from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from simulation.ema_macd_mp import run_ema_macd
from dateutil import parser
from infrastructure.collect_data import run_collection

if __name__ == '__main__':
    #api = OandaApi()
    instrumentCollection.LoadInstruments("./data")
    #run_collection(instrumentCollection, api)
    #run_ema_macd(instrumentCollection)
    run_ema_macd(instrumentCollection)
    
    #dfr = parser.parse("2021-04-21T01:00:00Z")
    #dto = parser.parse("2021-04-28T16:00:00Z")
    
    #df_candles = api.get_candles_df("EUR_USD", granularity="H1",
                                    #date_f=dfr, date_t=dto)
    
    #print(df_candles.head())
    #print()
    #print(df_candles.tail())
    #print(api.fetch_candles("EUR_USD", granularity="D", price="MB"))
    
    #instrumentCollection.CreateFile(api.get_account_instruments(), "./data")

    #instrumentCollection.PrintInstruments()
    #run_ma_sim(curr_list=["EUR", "USD", "GBP", "JPY", "AUD", "CAD"])