import os
import json

import discord
from discord.ext import commands

from dotenv import load_dotenv

# Load environment variables from the appropriate file
if os.path.exists('.env.development'):
    load_dotenv('.env.development')
else:
    load_dotenv('.env')

# Determine the environment
environment = os.getenv('ENVIRONMENT', 'production')
print(f"Running in {environment} environment.")

# Load configuration based on the environment
config_file = 'config.development.json' if environment == 'development' else 'config.json'

with open(config_file) as config_file:
    config = json.load(config_file)

BOT_TOKEN = config['discord_token']
PREFIXES = config.get('prefixes', ['!'])

intents = discord.Intents.default()
intents.message_content = True
intents.all()

# Prefixes to be used by the bot
def custom_prefixes(bot_name, msg):
    prefixes = PREFIXES
    return commands.when_mentioned_or(*prefixes)(bot_name, msg)


bot = commands.Bot(command_prefix=custom_prefixes, intents=intents)

# Load cogs when the bot is ready
@bot.event
async def on_ready():
    await bot.load_extension("cogs.musicCog")
    print("Ready!")


def main():
    bot.run(config['discord_token'])


if __name__ == "__main__":
    main()
