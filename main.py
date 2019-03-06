from multiprocessing import Process
import nyselib
import ast

symbols = ast.literal_eval(open('symbols.txt','r').read())

def one_minute():
    while 1:
        for symbol in symbols:
            rsi = nyselib.get_one_minute_rsi(symbol)
            if rsi<30:
                print("{}'s One Minute RSI is oversold, value = {}".format(symbol,rsi))
            if rsi<70:
                print("{}'s One Minute RSI is overbought, value = {}".format(symbol,rsi))

if __name__ == '__main__':
    Process(target=one_minute()).start()