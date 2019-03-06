import pandas as pd
from api import API_KEY

from alpha_vantage.timeseries import TimeSeries

ts = TimeSeries(key=API_KEY, output_format='pandas', indexing_type='date')
# Get json object with the intraday data and another with  the call's metadata

data, meta_data = ts.get_intraday(symbol='MSFT', interval='1min', outputsize='full')

print(data.head(-14))
