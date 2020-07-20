import discord
import os
from discord.ext import commands

# notes
# events: code that runs when the bot detects that a specific activity has happened

client = commands.Bot(command_prefix='.')


# on_read
# bot puts itself into a ready state
#
@client.event
async def on_ready():
    print('zoobot is online.')


# that loads the extension
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


# unloads the extension
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


# reloads cogs
# for any live updates on cogs
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')


# load all of the existing cogs
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')  # splicing off .py extension
        print(filename + ' has been loaded.')

# running the bot, passing in the discord token
client.run('NzM0ODU2MzU3MzcwMzk2Njky.XxXycg.N6Em7y1fhx6VDas_m8d4pfEIZsA')
