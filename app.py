from dotenv import load_dotenv
import os
import discord
from chatbots import DocomoChatBot

load_dotenv()

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if isinstance(message.channel, discord.DMChannel) \
        or client.user in message.mentions:
        # 個別チャットもしくは自分にメンションが来た場合のみ反応する

        bot = DocomoChatBot(os.getenv('DOCOMO_API_KEY'), os.getenv('DOCOMO_APP_ID'))

        await message.channel.send(bot.talk(message.content))

if __name__ == "__main__":
    client.run(os.getenv('DISCORD_TOKEN'))
