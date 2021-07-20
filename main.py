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
async def word(ctx, arg=None):

    if arg is None:
        await ctx.send(f"plx input number after command (e.g. !Word 5)")

    else:

        if not arg.isnumeric():
            await ctx.send("plx input number not characters after command (e.g. !Word 5)")

        if arg.isnumeric():
            wordlength_input = int(arg)
            randomword = random.choice(giveword) 
            max_tries = 5000
   
            while wordlength_input != len(randomword) and max_tries > 0:
                randomword = random.choice(giveword) 
                max_tries -= 1
                if max_tries == 0:
                    await ctx.send("no word found in a reasonable time. tip: try another number")
                    
            if wordlength_input == len(randomword):
                await ctx.send(randomword)

bot.run(os.environ['TOKEN'])

