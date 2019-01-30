import os
from dotenv import load_dotenv
load_dotenv()

import discord
from discord.ext import commands

import chalk
import datetime

bot = commands.Bot(command_prefix="!")

TOKEN = os.getenv('token')



@bot.event
async def on_ready():
    print(chalk.green(f"{bot.user.name} Online"))

@bot.event
async def on_message(message):

    pass

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

bot.run(TOKEN)
