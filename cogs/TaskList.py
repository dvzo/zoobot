import discord
import random

from discord.ext import commands, tasks


# configure background tasks
class TaskList(commands.Cog):
    # status for "Playing ..."
    game_list = ['bot games',
                 'with stream settings',
                 'with discord settings',
                 'calculators',
                 'programming games',
                 'algorithms',
                 'study games',
                 'ghost of sushi',
                 'need for speed',
                 'valorant',
                 'minesweeper',
                 'tetris',
                 'ms paint'
                 ]

    # status for "Listening to ..."
    music_list = ['kendrick lamar',
                  'blackpink',
                  'kanye west',
                  'juice wrld',
                  'charli xcx',
                  'playboi carti',
                  'twice',
                  'bts',
                  'james blake',
                  'red velvet',
                  'jpegmafia',
                  'death grips',
                  '21 savage',
                  'rosalia',
                  'travis scott',
                  'megan thee stallion',
                  'billie eilish'
                  ]

    movie_list = ['pulp fiction',
                  'alien',
                  'youtube videos',
                  'lisa <3',
                  'the departed',
                  'inglourious basterds',
                  'kill bill',
                  'reservoir dogs',
                  'kung fu hustle',
                  'silence of the lambs',
                  'the shining',
                  'twitch',
                  ]

    def __init__(self, client):
        self.client = client

    # change_status
    # changes status every 20 minutes to a random selection the 3 lists above
    @tasks.loop(minutes=20)
    async def change_status(self):
        rand_game = random.choice(self.game_list)
        rand_music = random.choice(self.music_list)
        rand_movie = random.choice(self.movie_list)
        rand_number = random.randint(1, 3)

        if rand_number == 1:
            await self.client.change_presence(activity=discord.Game(rand_game))
        elif rand_number == 2:
            await self.client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.listening, name=rand_music))
        elif rand_number == 3:
            await self.client.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name=rand_movie))

    # on_ready
    @commands.Cog.listener()
    async def on_ready(self):
        # starts the change_status loop
        self.change_status.start()


# setups this cog
def setup(client):
    client.add_cog(TaskList(client))
