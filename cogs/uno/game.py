from cogs.uno.deck import Card, Hand, Deck
from typing import Dict, List
from discord.ext import commands
import discord
#from time import sleep
import asyncio

class Uno:

    temp_bool: bool

    def __init__(self, bot):

        self.bot = bot
        self.temp_bool = False


    @commands.command
    async def uno(self, ctx, bet):

        #embed = discord.Embed(title="", description=f"", colour=discord.Color.green())
        #embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar_url)

        await ctx.send(embed=embed)

        self.temp_bool = True
        await asyncio.sleep(30)
        self.temp_bool = False

    @commands.command
    async def join(self, ctx):
        if self.temp_bool:
            pass
            #embed = discord.Embed(title="",description="",colour=discord.Color.green(),name= self.bot.user.name)
        pass


class unoGame:

    _players: List[str]
    _player_hands: Dict[str, Hand]
    temp_bool: bool
    play_deck: Deck
    drop_deck: Deck

    def __init__(self, players: List[str]):
        self._players = players
        self._player_hands = {}

        self.play_deck = Deck()
        self.play_deck.new_deck()
        self.play_deck.shuffle()

        self.drop_deck = Deck()


        for player in self._players:
            self._player_hands[player] = Hand()

    def start(self):

        for player in self._players:
            for i in range(7):
                self._player_hands[player].add(self.play_deck.remove())

        print (self._player_hands)


if __name__ == "__main__":

    a = unoGame(["bob","rob"])
    print(a)
    a.start()