import discord
from discord.ext import commands

import constants


BOT_TOKEN = constants.BOT_TOKEN

intents = discord.Intents.default()
intents.message_content = True
intents.all()


# Prefixes to be used by the bot
def custom_prefixes(botName, msg):
    prefixes = ['!']
    return commands.when_mentioned_or(*prefixes)(botName, msg)


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
