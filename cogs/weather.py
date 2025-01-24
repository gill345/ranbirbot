from datetime import datetime

import pytz as pytz
import requests
from discord.ext import commands


# Discord bot imports and API request import

# Weather cog
class Weather(commands.Cog):
    def __init__(self, bot, api_key):
        self.bot = bot
        self.api_key = api_key

    # Get weather for specified city by calling $weather city
    @commands.command(name='weather', help='Get weather information for a city')
    async def weather(self, ctx, *, city: str):
        # Url using api key and query string to get weather data from OpenWeatherMap
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={self.api_key}&units=metric"

        try:

            # Get response in json format

            response = requests.get(url).json()

            # Check for good response from API
            if response.get("cod") != 200:
                await ctx.send(f"City '{city}' not found.")
                return

            # Extract info from json
            weather = response["weather"][0]["description"]
            temp = response["main"]["temp"]
            feels_like = response["main"]["feels_like"]
            humidity = response["main"]["humidity"]
            wind = response["wind"]["speed"]
            timezone = response["timezone"]

            local_time = datetime.utcfromtimestamp(response['dt'] + timezone)
            local_time = pytz.utc.localize(local_time).astimezone(pytz.timezone('UTC'))
            formatted_time = local_time.strftime("%Y-%m-%d %H:%M:%S")

            # Emoji conditional on temperature in c
            if temp < 0:
                temp_emoji = "❄️🥶"
            elif 0 <= temp < 10:
                temp_emoji = "🧥🌬️"
            elif 10 <= temp < 20:
                temp_emoji = "🌤️🙂"
            elif 20 <= temp < 30:
                temp_emoji = "☀️😎"
            else:
                temp_emoji = "🔥🥵"

            await ctx.send(
                f"**Weather in {city.capitalize()}:** {temp_emoji}\n"
                f"**Condition:** {weather}\n"
                f"**Temperature:** {temp}°C (Feels like {feels_like}°C)\n"
                f"**Humidity:** {humidity}%\n"
                f"**Wind Speed:** {wind} m/s\n"
                f"Local Time: {formatted_time}"
            )
        except Exception as e:
            await ctx.send(f"Error fetching weather: {e}")


# Add weather cog
async def setup(bot):
    api_key = "apikey"  # Place your own OpenWeatherSource API key here
    await bot.add_cog(Weather(bot, api_key))
