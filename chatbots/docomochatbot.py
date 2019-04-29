import requests
import json
from datetime import datetime
from .chatbot import ChatBot

class DocomoChatBot(ChatBot):
    api_url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY='

    def __init__(self, api_key, app_id):
        self._api_url = DocomoChatBot.api_url + api_key
        self._app_id = app_id
        self._app_recv_time = datetime.now()


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
            'appRecvTime': "{0:%Y-%m-%d %H:%M:%S}".format(self._app_recv_time),
            'appSendTime': "{0:%Y-%m-%d %H:%M:%S}".format(datetime.now()),
        }

        response = requests.post(self._api_url, json.dumps(data), headers=headers)

        # 前回受信日時を更新
        self._app_recv_time = datetime.strptime(response.json()['serverSendTime'], 
            '%Y-%m-%d %H:%M:%S')

        return response.json()['systemText']['expression']
