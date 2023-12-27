from api.oanda_api import OandaApi
from infrastructure.instrument_collection import instrumentCollection
from simulation.ma_cross import run_ma_sim
from simulation.ema_macd_mp import run_ema_macd
from infrastructure.collect_data import run_collection

if __name__ == '__main__':
    
    instrumentCollection.LoadInstruments("./data")
    #run_collection(instrumentCollection, api)
    #run_ema_macd(instrumentCollection)
    run_ema_macd(instrumentCollection)
    
    #df_candles = api.get_candles_df("EUR_USD", granularity="H1",
                                    #date_f=dfr, date_t=dto)

    #print(df_candles.tail())
    #print(api.fetch_candles("EUR_USD", granularity="D", price="MB"))
    
    #instrumentCollection.CreateFile(api.get_account_instruments(), "./data")

    #run_ma_sim(curr_list=["EUR", "USD", "GBP", "JPY", "AUD", "CAD"])
