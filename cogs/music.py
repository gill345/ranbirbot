import discord
from discord.ext import commands
import yt_dlp as youtube_dl
# Bot imports and imports to process and play youtube-video audio

# Music cog
class Music(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Play music using $play youtubelink. Should work for most links
    @commands.command(name='play', help='To play song')
    async def play(self, ctx, url):

        # User voice channel at time of command call
        voice_channel = ctx.author.voice.channel if ctx.author.voice else None

        # Conditions for voice channel
        if not voice_channel:
            await ctx.send("You need to be in a voice channel to use this command.")
            return
        if not ctx.voice_client:
            await voice_channel.connect()

        # Error checking
        if not ctx.voice_client.is_connected():
            await ctx.send("Failed to connect to the voice channel.")
            return

        try:
            voice_client = ctx.voice_client
            async with ctx.typing():
                # Extract audio from YouTube using yt-dlp
                with youtube_dl.YoutubeDL({
                    'format': 'bestaudio/best',
                    'extractaudio': True,
                    'audioquality': 1,
                    'outtmpl': 'downloads/%(id)s.%(ext)s',  # Save audio temporarily
                    'restrictfilenames': True,
                    'noplaylist': True,
                    'quiet': True,
                }) as ydl:
                    info = ydl.extract_info(url, download=False)
                    audio_url = info['formats'][0]['url']  # Get the audio URL

                    # Audio URL error testing
                    print(f"Audio URL: {audio_url}")

                    # Play the audio from the URL
                    voice_client.play(discord.FFmpegPCMAudio(audio_url, executable=r"C:\Users\ranbi\Downloads\ffmpeg-master-latest-win64-gpl-shared\ffmpeg-master-latest-win64-gpl-shared\bin\ffmpeg.exe"))
                    await ctx.send(f'**Now playing:** {info["title"]}')

        except Exception as e:
            await ctx.send(f"An error occurred while trying to play the song: {e}")

    # Pause music output with $pause
    @commands.command(name='pause', help='This command pauses the song')
    async def pause(self, ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.pause()
            await ctx.send("The song has been paused. ⏸")
        else:
            await ctx.send("There is no song currently playing. 🤐")

    # Resume paused sog with $resume
    @commands.command(name='resume', help='This command resumes the song')
    async def resume(self, ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_paused():
            voice_client.resume()
            await ctx.send("The song has been resumed. ▶")
        else:
            await ctx.send("There is no paused song to resume. 🤐")

    # Stop current song with $stop
    @commands.command(name='stop', help='Stops the song')
    async def stop(self, ctx):
        voice_client = ctx.voice_client
        if voice_client and voice_client.is_playing():
            voice_client.stop()
            await ctx.send("The song has been stopped. 🛑")
        else:
            await ctx.send("There is no song currently playing. 🤐")

# Add music cog
async def setup(bot):
    await bot.add_cog(Music(bot))
