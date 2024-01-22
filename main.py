import os
os.system("pip install discord==1.7.3")
import discord
from discord.ext import commands
from colorama import Fore as f
import random 
import os
import time
prefix=input(f"{f.BLACK} ENTER PREFIX : P ")

aryanencrypt=my_secret = os.environ['token']#your token




client= commands.Bot(command_prefix=prefix,case_insensitive=True,self_bot=True,help_command=None)






@client.event
async def on_ready():
 os.system("clear")
 print(f"{f.RED}gg/flexcord")
 print(f"{f.GREEN}logged as {client.user.name}")
 print(f"{f.YELLOW}Prefix : {prefix}")
 print(f"{f.BLACK}{prefix}help for more info")
 
@client.command()
async def help(ctx):
  await ctx.send(f"**Auto OwO Bot\n{prefix}startowo\n{prefix}owohunt\n\n.gg/flexcord | MADE BY ARYAN**")
huh=[15,16,17,18,19,22,24,27,11,15,30,16,180]
@client.command()
async def startowo(ctx):
  aryan=["owo"]
  await ctx.message.delete()
  await ctx.send("starting auto owo uwu")
  while True:
    time.sleep(random.choice(huh))
    await ctx.send(random.choice(aryan))

@client.command()
async def owohunt(ctx):
  aryanxd=["owo"]
  await ctx.message.delete()
  while True:
    time.sleep(random.choice(huh))
    await ctx.send(random.choice(aryanxd))
client.run(aryanencrypt, bot=False)
