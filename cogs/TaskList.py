import discord
import random

from discord.ext import commands, tasks


# configure background tasks
class TaskList(commands.Cog):
    # read lists from files
    # status for "Playing ..."
    game_list_file = open("game_list_file.txt", "r")
    game_list = game_list_file.readlines()

    # status for "Listening to ..."
    music_list_file = open("music_list_file.txt", "r")
    music_list = music_list_file

    # status for "Watching ..."
    movie_list_file = open("movie_list_file", "r")
    movie_list = music_list_file

    def __init__(self, client):
        self.client = client

    # change_status
    # changes status every 5 minutes to a random selection the 3 lists above
    @tasks.loop(minutes=5)
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
