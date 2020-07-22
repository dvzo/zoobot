import discord
from discord import user
from discord.ext import commands


# list of events
class EventList(commands.Cog):

    def __init__(self, client):
        self.client = client

    # on_ready
    @commands.Cog.listener()
    async def on_ready(self):
        print('listener test.')




# setups this cog
def setup(client):
    client.add_cog(EventList(client))
