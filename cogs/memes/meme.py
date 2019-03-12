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

    @commands.command(aliases=["meme", "caption"])
    async def memes(self, ctx, meme_name="", *, word=" "):

        location = self.save_file()

        if caption.meme(meme_name, word, location):
            await ctx.send(file=discord.File(location))
        else:
            l = caption.all_memes()
            l = str(l)[10:-1]
            await ctx.send(f"Meme doesn't exist. Here is a list of all memes: {l}")


def setup(bot):
    bot.add_cog(Meme(bot))
