from multiprocessing import Process
import nyselib
import ast
import requests

bot_token = '791747943:AAFBMAXrJV_oIRQt6GmHfbUMaykyki6Sh2c'

url = "https://api.telegram.org/bot" + bot_token


def send_mess(text):
    params = {'chat_id': '-364692428', 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


symbols = ast.literal_eval(open('symbols.txt', 'r').read())


def one_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_one_minute_rsi(symbol)
                if rsi < 30:
                    response = "{}'s One Minute RSI is oversold, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
                if rsi > 70:
                    response = "{}'s One Minute RSI is overbought, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)

            except:
                continue


def five_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_five_minute_rsi(symbol)
                if rsi < 30:
                    response = "{}'s Five Minute RSI is oversold, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
                if rsi > 70:
                    response = "{}'s Five Minute RSI is overbought, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
            except:
                continue


def fifteen_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_fifteen_minute_rsi(symbol)
                if rsi < 30:
                    response = "{}'s Fifteen Minute RSI is oversold, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
                if rsi > 70:
                    response = "{}'s Fifteen Minute RSI is overbought, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
            except:
                continue


def thirty_minute():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_thirty_minute_rsi(symbol)
                if rsi < 30:
                    response = "{}'s Thirty Minute RSI is oversold, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
                if rsi > 70:
                    response = "{}'s Thirty Minute RSI is overbought, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
            except:
                continue


def one_day():
    while 1:
        for symbol in symbols:
            try:
                rsi = nyselib.get_one_day_rsi(symbol)
                if rsi < 30:
                    response = "{}'s Daily RSI is oversold, value = {}".format(symbol, rsi)
                    print("{}'s Daily RSI is oversold, value = {}".format(symbol, rsi))
                    send_mess(response)
                if rsi > 70:
                    response = "{}'s Daily RSI is overbought, value = {}".format(symbol, rsi)
                    print(response)
                    send_mess(response)
            except:
                continue


if __name__ == '__main__':
    Process(target=one_minute).start()
    Process(target=five_minute).start()
    Process(target=fifteen_minute).start()
    Process(target=thirty_minute).start()
    Process(target=one_day).start()
