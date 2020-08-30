#!/usr/bin/env python3
import json
import os
import logging
from discord.ext import commands
from commands.mute_command import MuteCommand

config = {}
logging.basicConfig()
logger = logging.getLogger()

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
    TOKEN = os.getenv('DISCORD_TOKEN')
    if (TOKEN is None):
        logger.warning('Environment token missing! Using token in config.')
        TOKEN = config['token']
    else:
        logger.warning('Environment token found! Using token in environment.')

    logger.warning(f'Starting bot using token: {TOKEN}')
    bot.run(TOKEN)