import discord
import random

from discord import channel, client
from discord.ext import commands


# list of commands
class CommandList(commands.Cog):
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

    def __init__(self, client):
        self.client = client

    # 8ball
    # grabs a random answer from responses
    @commands.command(aliases=['8ball'])
    async def _8ball(self, ctx, *, question):
        await ctx.send(f'```the 8ball says... \n\n{random.choice(self.responses)}```')

    # 8ball error handler
    @_8ball.error
    async def clear_8ball_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f':monkaHmm:\n```please enter a yes or no question```')

    # oops
    # a clear command that will remove the users' last sent message
    @commands.command()
    async def oops(self, ctx, amount=1):
        await ctx.channel.purge(limit=amount)

    # ping
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')


# setups this cog
def setup(client):
    client.add_cog(CommandList(client))
