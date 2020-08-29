from discord.ext import commands
from discord import Embed

async def set_mute_status(channel, status):
    """ The helper function that does the actual muting/unmuting """
    for user in channel.members:
        await user.edit(mute=status)

async def send_fancy_msg(channel, message):
    """ Sends a message to a text channel using an Embed """
    embed_msg = Embed(description=message, colour=0xFF0000)
    await channel.send(embed=embed_msg)

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def muteall(self, ctx):
        """ The command for muting users in a voice channel """
        userVoiceChannel = ctx.message.author.voice.channel
        await set_mute_status(userVoiceChannel, True)

        bot_msg = f"Users in {userVoiceChannel} have been muted."
        await send_fancy_msg(ctx.message.channel, bot_msg)

    @commands.command()
    async def unmuteall(self, ctx):
        """ The command for unmuting users in a voice channel. """
        userVoiceChannel = ctx.message.author.voice.channel
        await set_mute_status(userVoiceChannel, False)

        bot_msg = f"Users in {userVoiceChannel} have been unmuted."
        await send_fancy_msg(ctx.message.channel, bot_msg)