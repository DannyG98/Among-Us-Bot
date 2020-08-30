#!/usr/bin/env python3
import json
import os
from discord.ext import commands
from commands.mute_command import MuteCommand

config = {}

def load_configs():
    with open('config.json', 'r') as config_file:
        config = config_file.read()
        config = json.loads(config)
    return config

def initialize_config():
    global config
    config = load_configs()

def load_commands(bot):
    bot.add_cog(MuteCommand(bot))

if __name__ == '__main__':
    # Boilerplate stuff
    initialize_config()
    bot = commands.Bot(command_prefix = config['command_prefix'])
    load_commands(bot)

    # Check if an environment token exists. If not, resort to using config token
    TOKEN = os.getenv['DISCORD_TOKEN']
    if (TOKEN is None):
        TOKEN = config['token']

    bot.run(TOKEN)