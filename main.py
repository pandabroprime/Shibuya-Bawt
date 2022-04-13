import discord
import os
import time
import random
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '!') #put your own prefix here

@client.event
async def on_ready():
    print("HA! The Ultimate Art is Online!") #will print "bot online" in the console when the bot is online

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
      mQuote = ["I can all", "platforming videogames for the nintendo wii featuring 77 levels where you can", "wahoo", "You'll never be ballin'", "FUCKING BALLIN'", "bruh"]
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

    

    
      
  
    
    
@client.command()
async def ping(ctx):
    await ctx.send("pong!") #simple command so that when you type "!ping" the bot will respond with "pong!"

async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")

async def fuckoff(ctx):
    await ctx.send("Oh okay...")





client.run(os.getenv("TOKEN")) #get your bot token and create a key named `TOKEN` to the secrets panel then paste your bot token as the value. 
#to keep your bot from shutting down use https://uptimerobot.com then create a https:// monitor and put the link to the website that appewars when you run this repl in the monitor and it will keep your bot alive by pinging the flask server
#enjoy!
