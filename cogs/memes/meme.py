from typing import Dict, List
from discord.ext import commands
import caption
import os.path

import discord
import asyncio


class Meme:

    temp_bool: bool
    players: List[str]

    def __init__(self, bot):

        self.bot = bot
        self.temp_bool = False
        self.players = []
        self.location = os.path.dirname(__file__)

    def save_file(self):

        n = open("temp_img/num.txt", "r")
        s = int(n.readline())
        n.close()

        location = os.path.join(self.location, f"../../temp_img/temp{s}.png")

        n = open("temp_img/num.txt", "w")
        n.write(str((s + 1) % 3))
        n.close()

        return location

    @commands.command()
    async def twobuttons(self, ctx, *, word=""):

        captions = word.split(",")

        if len(captions) < 3:
            await ctx.send("Add more shit idiot")
            return

        location = self.save_file()

        caption.two_buttons(captions[0], captions[1], captions[2], location)

        await ctx.send(file=discord.File(location))

    @commands.command()
    async def talkidiot(self, ctx, *, word=""):

        captions = word.split(",")

        if len(captions) < 1:
            await ctx.send("All you had to do was add one caption")
            return

        location = self.save_file()

        caption.talk_idiot(captions[0], location)

        await ctx.send(file=discord.File(location))

    @commands.command()
    async def vr(self, ctx, *, word=""):

        captions = word.split(",")

        if len(captions) < 1:
            await ctx.send("All you had to do was add one caption")
            return

        location = self.save_file()

        caption.vr(captions[0], location)

        await ctx.send(file=discord.File(location))


def setup(bot):
    bot.add_cog(Meme(bot))
