import discord
import random

from discord import channel, client
from discord.ext import commands


# class that inherits from commands.Cog
class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # list of commands

    # 8ball
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        responses = ["It is certain.",
                     "It is decidedly so.",
                     "Without a doubt.",
                     "Yes - definitely.",
                     "You may rely on it.",
                     "As I see it, yes.",
                     "Most likely.",
                     "Outlook good.",
                     "Yes.",
                     "Signs point to yes.",
                     "Reply hazy, try again.",
                     "Ask again later.",
                     "Better not tell you now.",
                     "Cannot predict now.",
                     "Concentrate and ask again.",
                     "Don't count on it.",
                     "My reply is no.",
                     "My sources say no.",
                     "Outlook not so good.",
                     "Very doubtful."
                     ]

        await ctx.send(f'```the 8ball says... \n\n{random.choice(responses)}```')

    # oops
    # a clear command that will remove the users' last sent message
    @commands.command()
    async def oops(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    # ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')


# function to connect this to the bot
def setup(client):
    client.add_cog(Commands(client))
