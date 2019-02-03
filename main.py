import discord
from discord.ext import commands

import chalk
import datetime
import redis

import os
from dotenv import load_dotenv
load_dotenv()


r = redis.Redis.from_url(url="redis://:cWg97v6LkCWkkwZntYZEbocQ8DY0xlVG@redis-16113.c16.us-east-1-2.ec2.cloud.redislabs.com:16113/cavemanrockx-big-bot")
bot = commands.Bot(command_prefix="-", activity=discord.Game(name="Starting..."))
TOKEN = os.getenv('token')


@bot.event
async def on_ready():
    print(chalk.green(f"{bot.user.name} Online"))
    await bot.change_presence(activity=discord.Game(name=f"You"))


@bot.event
async def on_message(message):

    if message.author == bot.user:
        return

    await bot.process_commands(message)


@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")


@bot.command()
async def test(ctx, *, word = ""):
    embed = discord.Embed(title="", description=f"{word}", colour=discord.Color.green())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)

bot.run(TOKEN)
