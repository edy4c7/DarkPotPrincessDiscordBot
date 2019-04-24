import requests
import json
from .chatbot import ChatBot

class DocomoChatBot(ChatBot):
    api_url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY='

    def __init__(self, api_key, app_id):
        self._api_url = DocomoChatBot.api_url + api_key
        self._app_id = app_id
    

    def talk(self, message):
        headers = {
            'Crontent-Type': 'application/json; charset=UTF-8'
        }
        data = {
            'language': 'ja-JP',
            'botId': 'Chatting',
            'appId': self._app_id,
            'voiceText': message,
            'clientData': {
                'option': {
                    'birthdateY': '1992',
                    'birthdateM': '4',
                    'birthdateD': '2',
                    'sex': '女',
                    't': 'kansai'
                }
            },
            'appRecvTime': '2019-04-23 00:00:00',
            'appSendTime': '2019-04-23 00:01:00'
        }

        response = requests.post(self._api_url, json.dumps(data), headers=headers)

        return response.json()['systemText']['expression']
