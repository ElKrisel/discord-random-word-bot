import discord
from discord.ext import commands
import os
import random
import json


bot = commands.Bot(command_prefix='!')
client = discord.Client()

with open('words.json') as json_file:
    data = json.load(json_file)

giveword = data[random.choice(list(data))]


@bot.event
async def on_ready():
 print('we have logged in as Randoom-Bot'
  .format(client))

@bot.command()
async def test(ctx, arg):
  await ctx.send(arg)

@bot.command()
async def word(ctx, arg):

  if arg.isnumeric():

   wordlength_input = int(arg)
   randomword = random.choice(giveword) 
     
   while wordlength_input != len(randomword):
    randomword = random.choice(giveword) 
   if wordlength_input == len(randomword):
    await ctx.send(randomword)
 
  if not arg.isnumeric():
   await ctx.send("plx input number")


bot.run(os.environ['TOKEN'])

