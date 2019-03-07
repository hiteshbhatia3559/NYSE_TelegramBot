import requests

bot_token = '791747943:AAFBMAXrJV_oIRQt6GmHfbUMaykyki6Sh2c'

url = 'https://api.telegram.org/bot' + bot_token+'/'


def send_mess(text):
    params = {'chat_id': '-364692428', 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response

def get():
    response = requests.get(url+'getMe')
    return response

print(send_mess('Hi'))
