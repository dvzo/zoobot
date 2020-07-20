import discord
from discord.ext import commands


class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    # if you want to create an event in a cog, you need this decorator
    # self must be first parameter of every function your class takes
    # events
    @commands.Cog.listener()
    async def on_ready(self):
        print('listener test.')


# function to connect this to the bot
def setup(client):
    client.add_cog(Events(client))