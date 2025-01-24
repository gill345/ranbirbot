import asyncio
import discord
from discord.ext import commands
# Default Imports for Bot

# Give bot intent permissions
intents = discord.Intents.default()
intents.message_content = True

# Set all command prefixes to $
bot = commands.Bot(command_prefix="$", intents=intents)

# Load all cogs dynamically
async def load_cogs():
    await bot.load_extension("cogs.fun")
    await bot.load_extension("cogs.games")
    await bot.load_extension("cogs.music")
    await bot.load_extension("cogs.weather")

# Message to console to confirm login
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

# Login to bot using API key
async def main():
    async with bot:
        await load_cogs()

        # Place your own Discord Bot API key here
        await bot.start("apikey")

asyncio.run(main())