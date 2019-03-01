from typing import Dict, List
from discord.ext import commands
import discord
import asyncio


class Meme:

    temp_bool: bool
    players: List[str]

    def __init__(self, bot):

        self.bot = bot
        self.temp_bool = False
        self.players = []

    @commands.command()
    async def caption(self, ctx):


    @commands.command()
    async def unojoin(self, ctx):




def setup(bot):
    bot.add_cog(Uno(bot))
