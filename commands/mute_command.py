from discord.ext import commands
from discord import Embed

NO_SUCH_VC_MSG = "{}: Specified channel does not exist."
CHANNEL_VOICE_STATUS_MSG = "Users in {} have been {}."

async def set_mute_status(channel, status):
    """ The helper function that does the actual muting/unmuting """
    for user in channel.members:
        await user.edit(mute=status)

async def send_fancy_msg(channel, message, *args):
    """ Sends a message to a text channel using an Embed """
    embed_msg = Embed(description=message.format(*args), colour=0xFF0000)
    await channel.send(embed=embed_msg)

class MuteCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def muteall(self, ctx):
        """ The command for muting users in a voice channel """
        try:
            userVoiceChannel = ctx.message.author.voice.channel
            await set_mute_status(userVoiceChannel, True)
            await send_fancy_msg(ctx.message.channel, CHANNEL_VOICE_STATUS_MSG, userVoiceChannel, "muted")
        except AttributeError:
            await send_fancy_msg(ctx.message.channel, NO_SUCH_VC_MSG, ctx.message.author.mention)

    @commands.command()
    async def unmuteall(self, ctx):
        """ The command for unmuting users in a voice channel. """
        try:
            userVoiceChannel = ctx.message.author.voice.channel
            await set_mute_status(userVoiceChannel, False)
            await send_fancy_msg(ctx.message.channel, CHANNEL_VOICE_STATUS_MSG, userVoiceChannel, "unmuted")
        except AttributeError:
            await send_fancy_msg(ctx.message.channel, NO_SUCH_VC_MSG, ctx.message.author.mention)