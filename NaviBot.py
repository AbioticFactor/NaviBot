import asyncio
import discord
#from discord.ext import commands
#from discord.ext.commands import Bot
import random
from guide import guide

client = discord.Client()

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.upper().startswith("!NAVI"):
        game = str(message.author.game)
        await client.send_message(message.channel, message.author.mention +' '+ random.choice(['Hey!', 'Look!', 'Listen!']) 
        + '\n' + guide(game.replace(" ", "_")))
        

@client.event
async def on_ready():
    print('Ready...')

client.run('NDcwMTA2MDExMDcyNDYyODY5.DjTe4A.WPm9-SthnpvHp5OubdRpIpHhy68')