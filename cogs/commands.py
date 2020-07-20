import discord
from discord.ext import commands


# class that inherits from commands.Cog
class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('pong')


# function to connect this to the bot
def setup(client):
    client.add_cog(Commands(client))
