import discord
import os
from dotenv import load_dotenv

load_dotenv(os.path.join(os.getcwd(), ".env"))

client = discord.Client()

@client.event
async def on_ready():
    print("We've logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('Hello!'):
        await message.channel.send("Hello there!")

client.run(os.getenv('TOKEN'))