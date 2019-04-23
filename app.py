from dotenv import load_dotenv
import os
import discord
import datetime
import json
import requests

load_dotenv()

client = discord.Client()
api_url = 'https://api.apigw.smt.docomo.ne.jp/naturalChatting/v1/dialogue?APIKEY='\
    + os.getenv('DOCOMO_API_KEY')


@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user in message.mentions:
        # 自分にメンションが来た場合のみ反応する
        headers = {
            'Crontent-Type': 'application/json; charset=UTF-8'
        }
        data = {
            'language': 'ja-JP',
            'botId': 'Chatting',
            'appId': os.getenv('DOCOMO_APP_ID'),
            'voiceText': message.content,
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

        response = requests.post(api_url, json.dumps(data), headers=headers)

        await message.channel.send(response.json()['systemText']['expression'])

if __name__ == "__main__":
    client.run(os.getenv('DISCORD_TOKEN'))
