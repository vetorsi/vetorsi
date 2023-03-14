import discord
from googletrans import Translator

client = discord.Client()
translator = Translator()

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!translate '):
        text = message.content[11:]
        translation = translator.translate(text)

        await message.channel.send(f'{translation.origin} ({translation.src}) -> {translation.text} ({translation.dest})')

client.run('MTA4Mzg0ODQ4NjEyMzk5NTIzMA.GmCVLO.BCh9lmXu6yjvX3Imhfznp5VK7Sb0RuQ5nHYUic')
