import discord
from discord.ext import commands

import chalk
import datetime

import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix="-")

TOKEN = os.getenv('token')


@bot.event
async def on_ready():
    print(chalk.green(f"{bot.user.name} Online"))


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def test(ctx):
    embed = discord.Embed(title="", description="", colour=discord.Color.green())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

bot.run(TOKEN)
