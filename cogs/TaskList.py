import discord
import random

from discord.ext import commands, tasks


# configure background tasks
class TaskList(commands.Cog):
    game_list = []  # status for 'Playing ...'
    music_list = []  # status for 'Listening to ...'
    movie_list = []  # status for 'Watching ...'

    def __init__(self, client):
        self.client = client

    # change_status
    # changes status every 5 minutes to a random selection the 3 lists above
    @tasks.loop(seconds=10)
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
        # load text files on ready
        game_list_file = open("game_list_file.txt", "r")
        self.game_list = game_list_file.readlines()

        music_list_file = open("music_list_file.txt", "r")
        self.music_list = music_list_file.readlines()

        movie_list_file = open("movie_list_file.txt", "r")
        self.movie_list = movie_list_file.readlines()

        # starts the change_status loop
        self.change_status.start()


# setups this cog
def setup(client):
    client.add_cog(TaskList(client))
