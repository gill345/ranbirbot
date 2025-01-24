import asyncio
import random
from discord.ext import commands
# Default bot imports

# Array of random inspirational quote strings
quotes = [
    "The best way to predict the future is to create it. – Peter Drucker",
    "You miss 100% of the shots you don’t take. – Wayne Gretzky",
    "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
    "Don’t watch the clock; do what it does. Keep going. – Sam Levenson",
    "The only limit to our realization of tomorrow will be our doubts of today. – Franklin D. Roosevelt",
    "The harder you work for something, the greater you’ll feel when you achieve it. – Anonymous",
    "Dream big and dare to fail. – Norman Vaughan",
    "Don’t be pushed around by the fears in your mind. Be led by the dreams in your heart. – Roy T. Bennett",
    "Believe you can and you’re halfway there. – Theodore Roosevelt",
    "The only way to do great work is to love what you do. – Steve Jobs",
    "It always seems impossible until it’s done. – Nelson Mandela",
    "Do what you can, with what you have, where you are. – Theodore Roosevelt",
    "Start where you are. Use what you have. Do what you can. – Arthur Ashe",
    "Hardships often prepare ordinary people for an extraordinary destiny. – C.S. Lewis",
    "What lies behind us and what lies before us are tiny matters compared to what lies within us. – Ralph Emerson",
    "Act as if what you do makes a difference. It does. – William James",
    "Keep your face always toward the sunshine—and shadows will fall behind you. – Walt Whitman",
    "In the middle of every difficulty lies opportunity. – Albert Einstein",
    "Don’t limit your challenges. Challenge your limits. – Anonymous",
    "Success usually comes to those who are too busy to be looking for it. – Henry David Thoreau",
    "Opportunities don't happen. You create them. – Chris Grosser",
    "Don’t stop when you’re tired. Stop when you’re done. – Marilyn Monroe",
    "Go confidently in the direction of your dreams. Live the life you have imagined. – Henry David Thoreau",
    "Great things never come from comfort zones. – Anonymous",
    "You don’t have to be great to start, but you have to start to be great. – Zig Ziglar",
    "The only person you are destined to become is the person you decide to be. – Ralph Waldo Emerson",
    "Small steps in the right direction can turn out to be the biggest steps of your life. – Anonymous",
    "If you want something you’ve never had, you must be willing to do something you’ve never done. – Thomas Jefferson",
    "Fall seven times and stand up eight. – Japanese Proverb",
    "Strive not to be a success, but rather to be of value. – Albert Einstein",
]

# Choices in the game rock paper scissors
game1choices = ["rock", "paper", "scissors"]

# Fun cog
class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Invoke with $inspire to get a random quote fron the array
    @commands.command(name='inspire', help='Get an inspirational quote')
    async def inspire(self, ctx):
        await ctx.send(random.choice(quotes))

    # Start a game of rock paper scissors with $rpc. Pick within 30 seconds or game ends
    @commands.command(name='rpc', help='Play rock-paper-scissors')
    async def rpc(self, ctx):
        await ctx.send("Hmmm you dare challenge me, very well! Pick rock, paper, or scissors")

        # Check for valid input and from correct user
        def check(m):
            return m.author == ctx.author and m.content.lower() in game1choices

        try:

            # Extract user input and create a random option for the bot
            user_response = await self.bot.wait_for("message", check=check, timeout=30.0)
            user_choice = user_response.content.lower()
            bot_choice = random.choice(game1choices)

            # Condition check
            await ctx.send(f"I chose {bot_choice}!")
            if user_choice == bot_choice:
                await ctx.send("Why did you choose the same as me!?? 😐")
            elif (
                    (user_choice == "rock" and bot_choice == "scissors") or
                    (user_choice == "paper" and bot_choice == "rock") or
                    (user_choice == "scissors" and bot_choice == "paper")
            ):
                await ctx.send("NOOOOO YOU BEAT ME YOU CHEATED!!! 😭")
            else:
                await ctx.send("HA, You Tried!! 🤡😎")
        except asyncio.TimeoutError:
            await ctx.send("Too slow! You forfeited the game. 🤡😴")

# Add cog
async def setup(bot):
    await bot.add_cog(Fun(bot))
