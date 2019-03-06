from multiprocessing import Process
import nyselib
import ast
import time


bot_token = '791747943:AAFBMAXrJV_oIRQt6GmHfbUMaykyki6Sh2c'

symbols = ast.literal_eval(open('symbols.txt', 'r').read())


def one_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_one_minute_rsi(symbol)
                if rsi < 30:
                    print("{}'s One Minute RSI is oversold, value = {}".format(symbol, rsi))
                if rsi > 70:
                    print("{}'s One Minute RSI is overbought, value = {}".format(symbol, rsi))

            except:
                continue


def five_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_five_minute_rsi(symbol)
                if rsi < 30:
                    print("{}'s Five Minute RSI is oversold, value = {}".format(symbol, rsi))
                if rsi > 70:
                    print("{}'s Five Minute RSI is overbought, value = {}".format(symbol, rsi))
            except:
                continue


def fifteen_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_fifteen_minute_rsi(symbol)
                if rsi < 30:
                    print("{}'s Fifteen Minute RSI is oversold, value = {}".format(symbol, rsi))
                if rsi > 70:
                    print("{}'s Fifteen Minute RSI is overbought, value = {}".format(symbol, rsi))
            except:
                continue


def thirty_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_thirty_minute_rsi(symbol)
                if rsi < 30:
                    print("{}'s Thirty Minute RSI is oversold, value = {}".format(symbol, rsi))
                if rsi > 70:
                    print("{}'s Thirty Minute RSI is overbought, value = {}".format(symbol, rsi))
            except:
                continue


def one_day():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_one_day_rsi(symbol)
                if rsi < 30:
                    print("{}'s Daily RSI is oversold, value = {}".format(symbol, rsi))
                if rsi > 70:
                    print("{}'s Daily RSI is overbought, value = {}".format(symbol, rsi))
            except:
                continue


if __name__ == '__main__':
    Process(target=one_minute).start()
    Process(target=five_minute).start()
    Process(target=fifteen_minute).start()
    Process(target=thirty_minute).start()
    Process(target=one_day).start()
