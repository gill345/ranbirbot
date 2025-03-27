<h1>MonkeyBot</h1>

![discord](https://github.com/user-attachments/assets/091dcca5-383b-4d4d-9e19-5e27688e50dc)

## Overview
<p>MonkeyBot is a fairly simple yet fun discord bot that has access to a variety of games and commands. For example, MonkeyBot can play games such as rock paper scissors, or guess the number. Monkeybot
can also fetch the weather, inspire you with a quote or perhaps challenge you with some trivia. Additionally, MonkeyBot can play music in a voice channel using a YouTube link.</p>


## Commands
- `$guess <range>` - Guess a number between 1 and the specified range.
- `$rpc` - Play Rock, Paper, Scissors.
- `$trivia` - Answer trivia questions.
- `$inspire` - Get an inspirational quote.
- `$play <url>` - Play a YouTube audio and add to the queue.
- `$skip` - Skip the currently playing track.
- `$stop` - Stop music playback.
- `$weather <city>` - Get the weather of a city with local time.
- `$help` - Show all available commands and their descriptions.

  
## Setup
1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Install FFmpeg:
   - **Windows:** Download from [FFmpeg Official Site](https://ffmpeg.org/download.html) and add to PATH.
   - **Linux:** Use your package manager (`sudo apt install ffmpeg`)
   - **macOS:** Install with Homebrew (`brew install ffmpeg`)

4. Edit `bot.py` to set your Discord bot token and `weather.py` for your weather API key:
  
   In `bot.py`:
   ```python
   await bot.start("apikey")
   ```
In `cogs/weather.py`:
   ```python
   api_key = 'your_openweathermap_api_key_here'
   ```
   ```

## Usage
Start the bot:
```bash
python bot.py
```



## Contributing
Feel free to fork this project, submit issues, and create pull requests!

## License
This project is licensed under the MIT License.

