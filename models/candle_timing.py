import datetime as dt
from dateutil import tz

class CandleTiming:
    
    def __init__(self, last_time):
        self.last_time = last_time
        self.is_ready = False
        #self.from_zone = tz.tzutc()
        #self.to_zone = tz.tzlocal()
        #self.utc = dt.datetime.strptime(self.last_time, '%y-%m-%d %H:%M')
        #self.utc = self.utc.replace(tzinfo=self.from_zone)
        #self.central = self.utc.astimezone(self.to_zone)
        
    def __repr__(self):
        return f"last_candle:{dt.datetime.strftime(self.last_time, '%y-%m-%d %H:%M')} is_ready:{self.is_ready}"
        #return f"last_candle:{self.central} is_ready:{self.is_ready}"