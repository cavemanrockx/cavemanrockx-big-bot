from typing import Dict, List
from discord.ext import commands
from cogs.memes import caption
import os.path

import discord


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
    async def twobuttons(self, ctx, *, word="Putting enough captions,"
                                            + "Being a fucking idiot, You"):

        captions = word.split(",")

        if len(captions) < 3:
            word = "Putting enough captions,Being a fucking idiot, You"
            captions = word.split(",")

        location = self.save_file()

        caption.two_buttons(captions[0], captions[1], captions[2], location)

        await ctx.send(file=discord.File(location))

    @commands.command()
    async def talkidiot(self, ctx, *, word="I can't put captions on memes"):

        location = self.save_file()

        caption.talk_idiot(word, location)

        await ctx.send(file=discord.File(location))

    @commands.command()
    async def vr(self, ctx, *,
                 word="You can't even get this simple command right"):

        location = self.save_file()

        caption.vr(word, location)

        await ctx.send(file=discord.File(location))


def setup(bot):
    bot.add_cog(Meme(bot))
