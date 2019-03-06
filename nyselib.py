import pandas as pd
from api import API_KEY
import matplotlib.pyplot as plt
from alpha_vantage.techindicators import TechIndicators


def get_fifteen_minute_rsi(symbol):
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='15min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_five_minute_rsi(symbol):
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='5min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_one_minute_rsi(symbol):
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='1min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_thirty_minute_rsi(symbol):
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='30min', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])


def get_one_day_rsi(symbol):
    ti = TechIndicators(key=API_KEY, output_format='pandas')
    data, meta_data = ti.get_rsi(symbol=symbol, interval='daily', time_period=14)
    return int(data.tail(1).iloc[0]['RSI'])
