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

client = commands.Bot(command_prefix = '!')

shutUp = time.time()

#Prints message when bot is successfully online.
@client.event
async def on_ready():
    print("The Ultimate Art is Online!") 
    

@client.event
async def on_message(message):

    #No response if message is from this bot.  
    if message.author == client.user:
        return

    #No response if message is from another bot.
    if discord.utils.get(message.author.roles, name="Noise"):
        return

    #No response if bot is on "shutUp" cooldown.
    global shutUp
    if (shutUp - time.time() > 0):
        return

    #Sends message if Erik posts a spoilered message in shitpost channel.  
    if (message.channel.name == '#shitpost'):
      if (message.author.id == 713569164559908954 or message.author.id == 394751350140960769):
        if (message.attachments[0].is_spoiler()):
          await message.channel.send('^ This might have dicks. ^')


  
    msg = message.content

    #No response if message is meant for Music Bot or Mudae Bot.
    if msg.startswith('#') or msg.startswith('$'):
      return

    #The bot posts certain messages if it sees the following things in a message it reads.
    if 'madara uchiha' in msg.lower():
      await message.channel.send('Top Ten in the Server!')

    if 'kabuto' in msg.lower():
      await message.channel.send('Haha Shin you\'re just like Anko for real')

    if 'lugia' in msg.lower():
      print(shutUp)
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
      count.increase('deezNuts')

    if 'dragon' in msg.lower():
      await message.channel.send("it's tiring dragon deez balls down your throat")
      count.increase('deezNuts')

    if "wendy's" in msg.lower() or "wendys" in msg.lower():
      await message.channel.send("do you like wendy's balls are in your mouth")
      count.increase('deezNuts')

    if "i'm getting" in msg.lower():
      await message.channel.send('how about getting some bitches')

    if 'buru nyaa' in msg.lower():
      await message.channel.send('dori dori')

    if 'friend' in msg.lower():
      await message.channel.send('https://youtu.be/r6EPMvIhtyA')

    if 'nerf' in msg.lower():
      await message.channel.send('https://youtu.be/eH10efX7Png')

    if 'cena' in msg.lower():
      await message.channel.send('?????????')

    if 'gangster' in msg.lower():
      await message.channel.send('https://soundcloud.com/user-825338558/sasuke')

    if 'overwatch' in msg.lower():
      await message.channel.send('tf2 is better')

    if 'valorant' in msg.lower():
      await message.channel.send('ow is better')

    if 'rasengan' in msg.lower():
      await message.channel.send('https://media.discordapp.net/attachments/847934955275288596/953831647583813663/Screenshot_20220313-205214__01.jpg')

    if 'depressed' in msg.lower():
      await message.channel.send('https://cdn.discordapp.com/attachments/487383683267821578/926323619699777576/Snaptik_7045864609978289413_mayourin.mp4')

    if 'ramen' in msg.lower():
      await message.channel.send('https://cdn.discordapp.com/attachments/849818972694118430/955656957149212683/2022-03-21_22-38-21_Trim.mp4')

    if 'deidara' in msg.lower():
      await message.channel.send('Was I called?')

    if 'arizona' in msg.lower():
      await message.channel.send('https://cdn.discordapp.com/attachments/847934404487544882/965645248208453632/Im_From_A_R_I_Z_O_N_A.mp4')

    if 'fire' in msg.lower():
      await message.channel.send("Trust me Komasan the blue fire's cold")

    if 'the game' in msg.lower():
      await message.channel.send("https://youtu.be/bGzWicuI8n8")

    

    
    #Bot goes offline if command !fuckoff is used. Not functional when bot is on auto-deployment.
    if msg.startswith('!fuckoff'):
      await message.channel.send('Oh okay...')
      exit()

    #Bot returns count of deezNuts from deezNuts.txt file.
    if msg.startswith('!deeznuts'):
      await message.channel.send(str(count.get('deezNuts')))

    #Bot is unable to respond to messages form 5 minutes. Use when you plan on talking about a subject that might repeatedly ping the bot.
    if msg.startswith('!shutup'):
      await message.channel.send("Fine...but I'll be back in 5 minutes you fool!")
      shutUp = time.time() + 300

    #Sings happy birthday to the mentioned user.
    if msg.startswith('!happybirthday') and message.mentions:
      await message.channel.send("Happy birthday to you!")
      time.sleep(2)
      await message.channel.send("Happy birthday to you!")
      time.sleep(2)
      await message.channel.send("Happy birthday dear " + message.mentions[0].mention + "!")
      time.sleep(2)
      await message.channel.send("Happy birthday to you!")
      await message.channel.send('https://tenor.com/view/deidara-naruto-shippuden-naruto-yay-gif-4215383')

    #Add a suggestion to the suggestions.txt file!
    if msg.startswith('!suggest'):
      try:
        s = message.author.name + ": " + msg[9:]
        list.add(s, 'suggestions')
        await message.channel.send('Suggestion received!')
      except:
        await message.channel.send('Failed to receive suggestion.')

    if msg.startswith('shibuya!help'):
      r = open('README.md', 'r')
      ro = r.read()
      r.close()
      await message.channel.send(ro)
      



    
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
