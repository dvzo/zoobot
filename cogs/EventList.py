import discord
from discord import user
from discord.ext import commands


# list of events
class EventList(commands.Cog):
    emote_dict = {'KEKW': '<:KEKW:653684411069366288>',
                  'Pog': '<:Pog:600124616559689738>',
                  'PogU': '<:PogU:600124656598646806>',
                  'PogChamp': '<:PogChamp:556705814895788042>',
                  'POGGERS': '<:POGGERS:600124637275357194>',
                  'BibleThump': '<:BibleThump:539378160089956353>',
                  'scamTicket': '<:scamTicket:727675345439817728>',
                  'LUL': '<:LUL:550582087485489173>',
                  'HYPERS': '<:HYPERS:635856198540722196>',
                  'peepoSad': '<:peepoSad:720115528445984828>',
                  'peepoHappy': '<:peepoHappy:720115503645065328>',
                  'Gasp': '<:Gasp:557506419277168640>',
                  'FeelsBadMan': '<:FeelsBadMan:539400621334200320>',
                  'monkaS': '<:monkaS:556704950348939265>',
                  'monkaHmm': '<:monkaHmm:563891606546022400>',
                  'FeelsBirthdayMan': '<:FeelsBirthdayMan: 691778442416619551>'
                  }

    def __init__(self, client):
        self.client = client

    # on_command_error to handle cooldown errors
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        # checks if error is a cooldown error and sends the server a warning
        if isinstance(error, commands.CommandOnCooldown):
            cd_seconds = '%.2f' % error.retry_after
            await ctx.send(
                f'<:KEKW:653684411069366288>\n```this command is on cooldown for {cd_seconds} seconds```')

    # on_message listener for emojis
    @commands.Cog.listener()
    async def on_message(self, message):

        # don't want the bot to reply to itself
        if message.author == self.client.user:
            return

        # search through the emote list
        # if the message is just an emoji, react to it with that same emoji, and send it back as well
        if message.content in self.emote_dict.keys():
            emote_value = self.emote_dict[message.content]  # grab the value from the message as a key
            await message.channel.send(emote_value)


# setups this cog
def setup(client):
    client.add_cog(EventList(client))
