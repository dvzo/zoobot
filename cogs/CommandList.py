import discord
import random

from discord import channel, client, emoji
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
    @commands.cooldown(rate=1, per=5)
    async def _8ball(self, ctx, *, question):
        await ctx.send(f'```the 8ball says... \n\n{random.choice(self.responses)}```')

    # 8ball missing requirements error handler
    @_8ball.error
    async def _8ball_missing_argument_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f':monkaHmm:\n```please enter a yes or no question```')

    # oops
    # deletes last message of the user who called the oops command
    @commands.command()
    @commands.cooldown(rate=1, per=5)
    async def oops(self, ctx):

        # get the author of the user who ran the oops command
        oops_call = await ctx.channel.history(limit=1).get()
        oops_call_author = oops_call.author

        # always delete the oops command
        await ctx.channel.purge(limit=1)

        # grab the current message author after the oops command was deleted
        current_message = await ctx.channel.history(limit=1).get()
        current_message_author = current_message.author

        # if the user who called the oops command is the same as the most recent message, delete it
        if current_message_author == oops_call_author:
            await ctx.channel.purge(limit=1)

    # ping
    @commands.command()
    @commands.cooldown(rate=1, per=5)
    async def ping(self, ctx):
        await ctx.send('pong')


# setups this cog
def setup(client):
    client.add_cog(CommandList(client))
