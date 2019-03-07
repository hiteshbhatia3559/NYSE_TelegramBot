from api import API_KEY
from alpha_vantage.techindicators import TechIndicators
import time
import ast


def get_fifteen_minute_rsi(symbol):
    time.sleep(15)
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='15min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_five_minute_rsi(symbol):
    time.sleep(15)
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='5min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_one_minute_rsi(symbol):
    time.sleep(15)
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='1min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_thirty_minute_rsi(symbol):
    time.sleep(15)
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='30min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_one_day_rsi(symbol):
    time.sleep(15)
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='daily', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_four_hour_rsi(symbol):
    time.sleep(15)
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='60min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


# symbols = ast.literal_eval(open('symbols.txt', 'r').read())
# #
# # start = time.time()
# #
# # for item in symbols:
# #     print(get_thirty_minute_rsi(item))
# #     time.sleep(15)
# #
# # elapsed = time.time() - start
# #
# # print('time taken:'+str(elapsed))