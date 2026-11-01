# Beczka - A Self-hosted music bot for your Discord server

**Beczka** is a simple music bot for Discord, that runs 100% on your machine. Play any music from YouTube directly on your Discord server. Also supports playlists.

Nothing less, nothing more. Simple as. 

## Features

- **100% self-hosted** - Nothing ever leaves your device
- **Your own API key** - you have full control over what happens.
- **Play any music available on YouTube** - no matter the length.

## How does it work?

When you play music through Beczka, the following sequence of events happens:

   1. Audio from the provided YouTube URL is downloaded into 'audio.webm' file. You can find it in data/audio/ directory. 
   2. The bot then uses FFmpeg to turn audio from the file into Discord output.

It really is that simple. Nothing ever leaves your device, everything happens locally.

Only a single file ever gets stored on your machine - download only happens when it is needed, never before. When you get to the next track, the file is overwritten. 

## Available Commands

| Command | Description | 
|---------|-------------|
| `!play <url>` | Play a track or playlist from YouTube | 
| `!queue` | Show current queue (max 5 tracks) | 
| `!skip` | Skip currently playing track | 
| `!clear` | Clear the entire queue | 
| `!shuffle` | Randomly shuffle the queue | 
| `!leave` | Bot leaves the voice channel | 

## Quick Start

### Requirements
- Python 3.8 or higher
- pip (Python package manager)
- [FFmpeg](https://ffmpeg.org/)
- Discord bot token (from [Discord Developer Portal](https://discord.com/developers/applications))

### Installation

1. **Download the latest version** from [Releases](https://github.com/Meekr0/beczka/releases) and unzip it into a folder of your choice. 

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   You also might want to consider using a virtual environment to isolate any python dependencies.

  Windows: 
  ```bash
  python -m venv venv
  venv\Scripts\activate
  ```

  Linux/MacOs:
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```

3. **Configure the bot:**
   - Open .env with a text editor of your choice
   - Edit the following two variables:
   - `DISCORD_TOKEN`: Your bot token, generated from [Discord Developer Portal](https://discord.com/developers/applications)
   - `DISCORD_PREFIX`: Command prefix (default is `!`, i.e. `!play`)

4. **Run the bot:**
   ```bash
   python main.py
   ```

5. **Invite bot to your server:**
   - In Discord Developer Portal, go to "OAuth2" > "URL Generator"
   - Select permissions: `Send Messages`, `Connect`, `Speak`
   - Generate the URL and use it to add the bot to your server

## Usage

### Basic Commands

1. **Join voice channel** - simply use `!play` command while in a voice channel
2. **Play music:**
   ```
   !play <Youtube-Video-URL>
   ```

3. **Manage queue:**
   ```
   !queue       # Show queue
   !skip        # Skip track
   !clear       # Clear queue
   !shuffle     # Shuffle queue
   ```

4. **End session:**
   ```
   !leave       # Bot leaves voice channel
   ```

### Playlists

Bot automatically detects YouTube playlists. When using `!play` with a playlist link:
- All tracks from the playlist will be added to the queue
- Bot will inform you about the number of tracks added
- Playback will start from the first track

## Configuration

### Environment Variables

| Variable | Description | Default Value |
|----------|-------------|---------------|
| `DISCORD_TOKEN` | Discord bot token (required) | - |
| `DISCORD_PREFIX` | Bot command prefix | `!` |

### Multiple Prefixes

You can set multiple prefixes by separating them with commas:
```
DISCORD_PREFIX=!,?
```
Now the bot will respond to commands starting with `!` or `?`.

### How to Update?

1. Download the latest ZIP from Releases
2. Extract and replace old files
3. Install dependencies (if `requirements.txt` has changed):
   ```bash
   pip install -r requirements.txt
   ```
4. Restart the bot

### Supported Versions

All published versions are available in Releases. You can use older versions if the newer one doesn't work properly.

## Supported Platforms

Currently the bot only supports **YouTube**.

Future support is planned for Spotify and other services.

## Troubleshooting

In general, just **read the messages** the bot sends you. They should be more than enough to diagnose any issues you might encounter.

### Bot doesn't respond to commands
- Check if the bot has proper permissions on the server
- Make sure the command prefix is set correctly
- Check if the bot is online (should be visible as "Online" in the member list)

### Bot doesn't join voice channel
- Make sure **you** are in a voice channel
- Check if the bot has "Connect" permission in the channel
- Bot can only join channels it has access to

### Music doesn't play
- Check if the bot is in a voice channel
- Check if the video or playlist is public

### Installation dependency errors
- Make sure you have the latest pip installed:
  ```bash
  python -m pip install --upgrade pip
  ```

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Support

If you have questions, issues, or suggestions:
- Check the [Issues](https://github.com/Meekr0/beczka/issues) section
- Create a new issue with a description of the problem
- Include logs from terminal/powershell if possible

## AI Usage

Let me just start by saying that I am a professional software engineer. I am capable of writing code, and **Beczka** is not just vibe-coded slop. 

That being said, I did use some AI for coding purposes. This is primarily a hobby project for me, and a chance to learn some new tricks, as I am not that experienced in Python. 

All the designing and planning was done by me alone. Every line of code was thoroughly reviewed before being allowed into the project. 

All the ideas, especially the bad ones - are mine. I am always open to sugestions.

I do not consider **Beczka** to be *AI-slop*. But I am open to some of you considering it *human-slop*. This is the way of software engineering.

---

**Thank you for using Beczka!** 