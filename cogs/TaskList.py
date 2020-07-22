import discord
import random

from discord.ext import commands, tasks
from itertools import cycle


# configure background tasks
class TaskList(commands.Cog):
    # status for "Playing ..."
    playing_list = ['bot games',
                    'with stream settings',
                    'with discord settings',
                    'calculators',
                    'programming games',
                    'algorithms',
                    'study games',
                    'ghost of sushi',
                    'need for speed',
                    'valorant',
                    ''
                    ]

    # status for "Streaming ..."
    streaming_list = []

    def __init__(self, client):
        self.client = client

    # change_status
    # changes status every 10 seconds to a random selection of playing_list
    @tasks.loop(seconds=10)
    async def change_status(self):
        play_activity = random.choice(self.playing_list)
        await self.client.change_presence(activity=discord.Game(play_activity))
        # await self.client.change_presence(activity=discord.Game(next(self.statusList)))

    # on_ready
    @commands.Cog.listener()
    async def on_ready(self):
        self.change_status.start()
        print('tasks is ready')


# setups this cog
def setup(client):
    client.add_cog(TaskList(client))
