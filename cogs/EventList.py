import discord
from discord import user
from discord.ext import commands


# list of events
class EventList(commands.Cog):

    def __init__(self, client):
        self.client = client

    # general error handler
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # checks if error is a cooldown error and sends the server a warning
        if isinstance(error, commands.CommandOnCooldown):
            cd_seconds = '%.2f' % error.retry_after
            await ctx.send(
                f'<:KEKW:735575259910111362>\n```this command is on cooldown for {cd_seconds} seconds```')

    # emoji listener
    @commands.Cog.listener()
    async def on_message(self, message):

        # don't want the bot to reply to itself
        if message.author == self.client.user:
            return

        # if message is KEKW, send back KEKW
        if message.content == '<:KEKW:735575259910111362>':
            # await message.add_reaction('<:KEKW:735575259910111362>') # adds a reaction
            await message.channel.send(f'<:KEKW:735575259910111362>')


# setups this cog
def setup(client):
    client.add_cog(EventList(client))
