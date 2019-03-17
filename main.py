import discord
from discord.ext import commands

import chalk
import datetime
import redis

import os
from dotenv import load_dotenv
load_dotenv()

#MemeBot
#https://discordapp.com/oauth2/authorize?client_id=555164340999815230&scope=bot&permissions=515136
#BigBot
#https://discordapp.com/oauth2/authorize?client_id=537345378702589993&scope=bot&permissions=8

r = redis.Redis.from_url(url="redis://:cWg97v6LkCWkkwZntYZEbocQ8DY0xlVG@redis-16113.c16.us-east-1-2.ec2.cloud.redislabs.com:16113/cavemanrockx-big-bot")
bot = commands.Bot(command_prefix="-", activity=discord.Game(name="Starting...")
                   , case_insensitive=True)
extensions = ["memes.meme"]
TOKEN = os.getenv('token')

img_num = 0


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


@bot.command(aliases=["say"])
async def echo(ctx, *, word=""):
    embed = discord.Embed(title="", description=f"{word}", colour=discord.Color.green())
    embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

    await ctx.send(embed=embed)


@bot.command()
async def time(ctx):
    date = str(datetime.datetime.today())
    date = date.split(".")
    date = date[0]
    embed = discord.Embed(title="", description=f"{date} [EST]", colour=discord.Color.green())
    embed.set_author(name="Time")

    await ctx.send(embed=embed)


@bot.command()
async def reload(ctx):

    for extension in extensions:
        try:
            bot.unload_extension(f"cogs.{extension}")
            print(chalk.green(f"cogs.{extension} unloaded"))
            await ctx.send(f"cogs.{extension} unloaded")

            bot.load_extension(f"cogs.{extension}")
            print(chalk.green(f"cogs.{extension} loaded"))
            await ctx.send(f"cogs.{extension} loaded")

        except Exception as error:
            print(chalk.red(f"{extension} cannot be loaded. {error}"))

# @bot.command()
# async def load(extension):
#     try:
#         bot.load_extension(f"cogs.{extension}")
#         print(chalk.green(f"cogs.{extension} loaded"))
#     except Exception as error:
#         print(chalk.red(f"{extension} cannot be loaded. {error}"))

@bot.command()
async def unload(extension):
    try:
        bot.unload_extension(f"cogs.{extension}")
        print(chalk.green(f"cogs.{extension} unloaded"))
    except Exception as error:
        print(chalk.red(f"{extension} cannot be unloaded. {error}"))


if __name__ == "__main__":
    for extension in extensions:
        try:
            bot.load_extension(f"cogs.{extension}")
        except Exception as error:
            print(chalk.red(f"{extension} cannot be loaded. {error}"))

    bot.run(TOKEN)
