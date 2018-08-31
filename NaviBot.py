import asyncio
import discord
#from discord.ext import commands
#from discord.ext.commands import Bot
import random
from guide import guide
from achieve import achieve
from cheats import cheats

client = discord.Client()

@client.event
async def on_message(message):
    
    gamename = str(message.author.game)

    if message.author == client.user:
        return

    if message.content.upper().startswith("!NAVI GUIDE"):  
        embed = discord.Embed(
            title=random.choice(['Hey!', 'Look!', 'Listen!']),
            description=guide(gamename.replace(" ", "_"))+'\n' + message.author.mention,
            color=discord.Color.blue()
            )

        await client.send_message(message.channel, embed=embed)
    
    if message.content.upper().startswith("!NAVI ACHIEVEMENTS"):
        embed = discord.Embed(
            title=random.choice(['Hey!', 'Look!', 'Listen!']),
            description=achieve(gamename)+'\n'+'\n'+message.author.mention,
            color=discord.Color.blue()
            )
        await client.send_message(message.channel, embed=embed)

    if message.content.upper().startswith("!NAVI CHEATS"):
        embed = discord.Embed(
            title=random.choice(['Hey!', 'Look!', 'Listen!']),
            description=cheats(gamename)+'\n'+'\n'+message.author.mention,
            color=discord.Color.blue()
            )

        await client.send_message(message.channel, embed=embed)


@client.event
async def on_ready():
    print('Ready...')

client.run('NDcwMTA2MDExMDcyNDYyODY5.DjTe4A.WPm9-SthnpvHp5OubdRpIpHhy68')