from typing import Dict, List
from discord.ext import commands
import discord
from cogs.uno.game import unoGame
import asyncio


class Uno:

    temp_bool: bool
    players: List[str]

    def __init__(self, bot):

        self.bot = bot
        self.temp_bool = False
        self.players = []

    @commands.command()
    async def uno(self, ctx, bet=0):

        embed = discord.Embed(title="", description=f"Uno game has started. Type {ctx.prefix}unojoin to join.", colour=discord.Color.red())
        embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

        await ctx.send(embed=embed)
        self.players.append(ctx.author.name)

        self.temp_bool = True
        await asyncio.sleep(10)
        self.temp_bool = False

        # Checks if there is enough players for the game
        if len(self.players) < 2:

            not_enough = discord.Embed(title="", description=f"Not enough player joined. Game canceled.", colour=discord.Color.red())
            await ctx.send(embed=not_enough)

            self.players.clear()
            return

        # If there are enough players
        enough = discord.Embed(title="", description=f"The game has started.", colour=discord.Color.green())
        await ctx.send(embed=enough)

        game = unoGame(self.players)
        game.start()

        guild = ctx.message.guild
        await guild.create_text("uno")

        player = self.players[0]



        #while True:
            #hand = game.show_hand(player)
            #show prompt in channel of player to pick card.
            #game.try_drop( player, card)



        self.players.clear()

    @commands.command()
    async def unojoin(self, ctx):
        if self.temp_bool:
            if ctx.author.name not in self.players:
                self.players.append(ctx.author.name)
            else:
                embed = discord.Embed(title="", description=f"You are already in the game.", colour=discord.Color.red())
                await ctx.send(embed=embed)
                return

            embed = discord.Embed(title=f"{ctx.author.name} has joined the game", description=f"Players: {self.players}", colour=discord.Color.green())
            embed.set_author(name=self.bot.user.name, icon_url=self.bot.user.avatar_url)

            await ctx.send(embed=embed)
            return
        embed = discord.Embed(title=f"", description=f"You need to start a game first", colour=discord.Color.red())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Uno(bot))