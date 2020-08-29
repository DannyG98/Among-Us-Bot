#!/usr/bin/env python3
import json
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
    initialize_config()
    bot = commands.Bot(command_prefix = config['command_prefix'])
    load_commands(bot)
    bot.run(config['token'])