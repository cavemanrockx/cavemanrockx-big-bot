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
        caption.catalog()
        self.catalog_loc = os.path.join(self.location, f"../../temp_img/catalog.png")

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
    async def memes(self, ctx, meme_name="help", *, word=""):

        location = self.save_file()

        if meme_name.strip(" ").lower() == "help":
            await ctx.send(file=discord.File(self.catalog_loc))

        elif meme_name.strip(" ").lower() == "customtoptext":
            if len(ctx.message.attachments) > 0:
                url = ctx.message.attachments[0].url

            elif len(word.split(",")) > 1:
                temp_word = word.split(",")[0]
                temp_word = temp_word.strip(" ")
                url = temp_word
                word = word[word.index(",")+1:]
            else:
                await ctx.send(f"Please input a valid link or image attachment "
                               f"and caption")
                await ctx.send(f"Usage: -meme customtoptext url, caption or")
                await ctx.send(f"-meme customtoptext caption (with an attachment)")
                return

            if caption.customtoptext(url, word, location):
                await ctx.send(file=discord.File(location))
            else:
                await ctx.send(f"Please input a valid link or image attachment")

        elif caption.meme(meme_name, word, location):
            await ctx.send(file=discord.File(location))
        else:
            l = caption.all_memes()
            l = str(l)[1:-1]
            await ctx.send(f"Meme doesn't exist. Here is a list of all memes: {l}")

    @commands.command()
    async def seal(self, ctx, *, url=""):

        location = self.save_file()
        if len(ctx.message.attachments) > 0:
            url = ctx.message.attachments[0].url
        else:
            url = url

        if caption.seal(url, location):
            await ctx.send(file=discord.File(location))
        else:
            await ctx.send(f"Please input a valid link or image attachment")

def setup(bot):
    bot.add_cog(Meme(bot))
