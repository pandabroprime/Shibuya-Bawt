import discord
import os
import time
import random
from tools import count
from tools import list
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("bot online") #will print "bot online" in the console when the bot is online

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if discord.utils.get(message.author.roles, name="Noise"):
        return

    msg = message.content

    if 'madara uchiha' in msg.lower():
        await message.channel.send('Top Ten in the Server!')

    if 'kabuto' in msg.lower():
      await message.channel.send('Haha Shin you\'re just like Anko for real')

    if 'lugia' in msg.lower():
      await message.channel.send("people should not eat pokemon :\)")

    if 'mario' in msg.lower():
      mQuote = list.toList('marioQuotes')
      await message.channel.send('@kirby012#0039 ' + random.choice(mQuote))

    if 'sweet' in msg.lower():
      await message.channel.send('Get to the **ambush** before your brother is killed.')
  
    if 'reshiram' in msg.lower():
      await message.channel.send('lubby chudder')

    if 'shocker' in msg.lower():
      await message.channel.send('https://youtu.be/sMk-HPBF6Mw')

    if 'pain' in msg.lower():
        await message.channel.send("that's what they call me")

    if 'snartle' in msg.lower():
        await message.channel.send('rage, fury.')

    if "how did that happen" in msg.lower() or "how'd that happen" in msg.lower():
        await message.channel.send('yo ho ho he took a bite of gum gum')

    if 'tobirama' in msg.lower():
        await message.channel.send('chakrrrrrrrrrrrrrrrrra')

    if 'penis' in msg.lower():
        await message.channel.send('https://naruto.fandom.com/wiki/Genma_Shiranui')

    if 'candace' in msg.lower():
        await message.channel.send('candace dick fit in your mouth')

    if 'dragon' in msg.lower():
        await message.channel.send("it's tiring dragon deez balls down your throat")

    if "wendy's" in msg.lower() or "wendys" in msg.lower():
        await message.channel.send("do you like wendy's balls are in your mouth")

    if 'getting' in msg.lower():
        await message.channel.send('how about getting some bitches')

    if 'buru nyaa' in msg.lower():
        await message.channel.send('dori dori')

    if 'friend' in msg.lower():
        await message.channel.send('https://youtu.be/r6EPMvIhtyA')

    if msg.startswith('!fuckoff'):
        await message.channel.send('Oh okay...')
        exit()

    if msg.startswith('!deeznuts'):
        await message.channel.send(str(count.get('deezNuts')))


    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")







client.run(os.getenv("TOKEN"))
