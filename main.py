import discord
import os
import requests
from dotenv import load_dotenv
import json
import logging
import random
import youtube_dl

load_dotenv(os.path.join(os.getcwd(), ".env"))

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    # bind to ipv4 since ipv6 addresses cause issues sometimes
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn'
}

sad_words = ["sad", "depressed", "unhappy", "angry", "miserable"]
starter_encouragements = [
    "Cheer up!",
    "Hang in there.",
    "You are a great person / bot!"
]

client = discord.Client()
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


def get_data():
    response = requests.get('https://zenquotes.io/api/random')
    json_data = json.loads(response.text)
    quote = json_data[0]['q'] + " - " + json_data[0]['a']
    return quote

@client.event
async def on_ready():
    print("We've logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    msg = message.content

    if message.author == client.user:
        return
    
    if message.content.startswith('!!inspire'):
        quote = get_data()
        await message.channel.send(quote)
    
    if any(word in msg for word in sad_words):
        await message.channel.send(random.choice(starter_encouragements))

client.run(os.getenv('TOKEN'))
