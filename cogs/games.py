import asyncio
import random
from discord.ext import commands
# Default bot imports

# Dictionary of various trivia questions
triviaQuestions = [
    {
        'question': "What is the capital of France?",
        'choices': ['A) Berlin', 'B) Madrid', 'C) Paris', 'D) Rome'],
        'answer': 'C'
    },
    {
        'question': "What is the largest planet in our solar system?",
        'choices': ['A) Earth', 'B) Jupiter', 'C) Saturn', 'D) Mars'],
        'answer': 'B'
    },
    {
        'question': "Which language is primarily used for web development?",
        'choices': ['A) Python', 'B) Java', 'C) JavaScript', 'D) C++'],
        'answer': 'C'
    },
    {
        'question': "Who wrote 'Romeo and Juliet'?",
        'choices': ['A) Shakespeare', 'B) Dickens', 'C) Austen', 'D) Hemingway'],
        'answer': 'A'
    },
    {
        'question': "What is the smallest country in the world?",
        'choices': ['A) Monaco', 'B) Vatican City', 'C) San Marino', 'D) Liechtenstein'],
        'answer': 'B'
    },
    {
        'question': "In what year did the Titanic sink?",
        'choices': ['A) 1912', 'B) 1905', 'C) 1920', 'D) 1898'],
        'answer': 'A'
    },
    {
        'question': "What is the chemical symbol for gold?",
        'choices': ['A) Au', 'B) Ag', 'C) Pb', 'D) Fe'],
        'answer': 'A'
    },
    {
        'question': "Which planet is known as the Red Planet?",
        'choices': ['A) Mars', 'B) Venus', 'C) Saturn', 'D) Jupiter'],
        'answer': 'A'
    },
    {
        'question': "Who painted the Mona Lisa?",
        'choices': ['A) Van Gogh', 'B) Da Vinci', 'C) Picasso', 'D) Michelangelo'],
        'answer': 'B'
    },
    {
        'question': "Which country is the largest producer of coffee?",
        'choices': ['A) Brazil', 'B) Colombia', 'C) Vietnam', 'D) Indonesia'],
        'answer': 'A'
    },
    {
        'question': "What is the tallest mountain in the world?",
        'choices': ['A) K2', 'B) Mount Everest', 'C) Kilimanjaro', 'D) Denali'],
        'answer': 'B'
    },
    {
        'question': "Which animal is known as the 'King of the Jungle'?",
        'choices': ['A) Elephant', 'B) Lion', 'C) Tiger', 'D) Gorilla'],
        'answer': 'B'
    },
    {
        'question': "Who was the first man to step on the moon?",
        'choices': ['A) Buzz Aldrin', 'B) John Glenn', 'C) Neil Armstrong', 'D) Michael Collins'],
        'answer': 'C'
    },
    {
        'question': "What is the name of the longest river in the world?",
        'choices': ['A) Nile', 'B) Amazon', 'C) Yangtze', 'D) Mississippi'],
        'answer': 'A'
    },
    {
        'question': "Which movie won the Oscar for Best Picture in 1994?",
        'choices': ['A) Forrest Gump', 'B) The Shawshank Redemption', 'C) Pulp Fiction', 'D) Braveheart'],
        'answer': 'A'
    },
    {
        'question': "Who invented the telephone?",
        'choices': ['A) Nikola Tesla', 'B) Thomas Edison', 'C) Alexander Graham Bell', 'D) Albert Einstein'],
        'answer': 'C'
    },
    {
        'question': "Which famous scientist developed the theory of relativity?",
        'choices': ['A) Isaac Newton', 'B) Albert Einstein', 'C) Galileo Galilei', 'D) Charles Darwin'],
        'answer': 'B'
    },
    {
        'question': "What is the most widely spoken language in the world?",
        'choices': ['A) English', 'B) Spanish', 'C) Mandarin Chinese', 'D) Hindi'],
        'answer': 'C'
    },
    {
        'question': "What year did World War II end?",
        'choices': ['A) 1942', 'B) 1945', 'C) 1950', 'D) 1960'],
        'answer': 'B'
    },
    {
        'question': "Which country is known as the Land of the Rising Sun?",
        'choices': ['A) South Korea', 'B) Japan', 'C) China', 'D) India'],
        'answer': 'B'
    },
    {
        'question': "Which famous fictional detective resides at 221B Baker Street?",
        'choices': ['A) Hercule Poirot', 'B) Sherlock Holmes', 'C) Sam Spade', 'D) Miss Marple'],
        'answer': 'B'
    },
    {
        'question': "What is the largest ocean on Earth?",
        'choices': ['A) Atlantic Ocean', 'B) Indian Ocean', 'C) Southern Ocean', 'D) Pacific Ocean'],
        'answer': 'D'
    }
]

# Games cog
class Games(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Guess the number game, invoked by $guess x. Unlimited tries within 30 seconds.
    @commands.command(name='guess', help='Guess a number between 1 and a given range')
    async def guess(self, ctx, numrange: int):

        # Numbers under 2 including negative numbers not allowed
        if numrange < 2:
            await ctx.send("The range must be 2 or higher! 🤨")
            return

        await ctx.send(f"Okay, Im thinking of a number between 1 and {numrange}, can you guess it? 😉")

        # Generate random number between 1 and user defined range
        number = random.randint(1, numrange)

        # Loop until user gets number or 30 seconds run out
        while True:
            try:
                guess = await self.bot.wait_for(
                    # Check for valid input and from correct user
                    'message', check=lambda m: m.author == ctx.author, timeout=30.0
                )
                guess = int(guess.content)

                if guess == number:
                    await ctx.send("You Got IT!?? 😲")
                    break
                else:
                    await ctx.send(f"Nope {guess} is wrongggg, try again!! 🤡😎")
            except asyncio.TimeoutError:
                await ctx.send("You took too long. Game over! 🤡😴")
                break

    # Trivia game with $trivia. Randomly selects question from dictionary and gives user 30 sec to answer
    @commands.command(name='trivia', help='Start a trivia quiz game.')
    async def trivia(self, ctx):

        # Randomly select a question
        question = random.choice(triviaQuestions)

        await ctx.send(f"✨ **Trivia Time!** ✨\n{question['question']}")
        await ctx.send("\n".join(question['choices']))

        def check(m):
            return m.author == ctx.author and m.content.lower() in ['a', 'b', 'c', 'd']

        try:
            msg = await self.bot.wait_for('message', check=check, timeout=30.0)

            if msg.content.upper() == question['answer']:
                await ctx.send(f"Correct! Answer was: {question['answer']}. Hmmmm you're smart 🤔")
            else:
                await ctx.send(f"Wrong! The correct answer was: {question['answer']} 🤭")
        except asyncio.TimeoutError:
            await ctx.send("Time's up! You didn't answer in time. 🙄")

    # End trivia game early with $endgame
    @commands.command(name='endgame', help='End your current trivia game.')
    async def endgame(self, ctx):
        await ctx.send("The trivia game has been ended. 🤐")

    @commands.command(name='helpme', help='List all available commands')
    async def helpme(self, ctx):
        help_text = (
            "**Bot Commands:**\n\n"
            "🙉 **Weather Commands:**\n"
            "`!weather <city>` - Get current weather for a given city\n\n"
            "🙉 **Fun & Game Commands:**\n"
            "`!inspire` - Get an inspirational quote\n"
            "`!rpc` - Play Rock-Paper-Scissors\n"
            "`!guess <range>` - Guess a number between 1 and the range\n"
            "`!trivia` - Answer a trivia question\n"
            "`!endgame` - End the current trivia game\n\n"
            "🙉 **Music Commands:**\n"
            "`!play <song name or URL>` - Play a song in the voice channel\n"
            "`!pause` - Pause the currently playing song\n"
            "`!resume` - Resume the paused song\n"
            "`!stop` - Stop the song and disconnect from the voice channel\n"
        )

        await ctx.send(help_text)

# Setup cog
async def setup(bot):
    await bot.add_cog(Games(bot))