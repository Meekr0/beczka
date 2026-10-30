import os

import discord
from discord.ext import commands

from dotenv import load_dotenv

# Load environment variables from the appropriate file
# Priority: .env.development > .env
if os.path.exists('.env.development'):
    load_dotenv('.env.development')
elif os.path.exists('.env'):
    load_dotenv('.env')

# Determine the environment
environment = os.getenv('ENVIRONMENT', 'production')
print(f"Running in {environment} environment.")

# Load configuration from environment variables
BOT_TOKEN = os.getenv('DISCORD_TOKEN')
PREFIXES = os.getenv('DISCORD_PREFIX', '!').split(',') if ',' in os.getenv('DISCORD_PREFIX', '!') else [os.getenv('DISCORD_PREFIX', '!')]

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
    bot.run(BOT_TOKEN)


if __name__ == "__main__":
    main()
