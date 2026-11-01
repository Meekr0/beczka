import asyncio
import discord
import random
from discord.ext import commands
from services.youtube.youtube_service import YouTubeService

queue = []
current_url = None

AUDIO_FILE_PATH = './data/audio/audio.webm'

async def playNext(ctx, vc):
    global current_url
    if queue:
        current_url = queue.pop(0)
        title = await YouTubeService.get_title(current_url)
        isAudioDownloaded = await YouTubeService.download_audio(current_url, AUDIO_FILE_PATH)
        if isAudioDownloaded:
            await ctx.send(f'Now playing: {title}')
            vc.play(discord.FFmpegPCMAudio(AUDIO_FILE_PATH), after=lambda e: asyncio.run_coroutine_threadsafe(playNext(ctx, vc), vc.loop))
        else:
            await ctx.send("Couldn't download the file")
            if queue:
                await playNext(ctx, vc)
            else:
                await ctx.send("Queue is empty, leaving the channel...")
                await vc.disconnect()
    else:
        current_url = None
        await ctx.send("Queue is empty, leaving the channel...")
        await vc.disconnect()


class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("MusicCog Ready")

    @commands.command()
    async def play(self, ctx, *, url: str):

        # Check if user is in a voice channel
        if ctx.author.voice is None or ctx.author.voice.channel is None:
            await ctx.send("Join a voice channel first.")
            return

        # Connect to voice channel
        vc = ctx.author.voice.channel
        currentChannel = ctx.voice_client
        if currentChannel is None:
            vc = await vc.connect()
        else:
            vc = currentChannel

        queue.append(url)
        title = await YouTubeService.get_title(url)

        if vc.is_playing():
            await ctx.send(f'{title} added to queue')
        else:
            await playNext(ctx, vc)

    @commands.command()
    async def leave(self, ctx):
        vc = ctx.voice_client
        if vc is not None:
            await vc.disconnect()
            await ctx.send("Leaving the voice channel.")
        else:
            await ctx.send("I'm not in a voice channel.")

    @commands.command()
    async def queue(self, ctx):
        if queue:
            msg = await self.generateQueue(limit=5)
            await ctx.send(msg)
        else:
            await ctx.send("The queue is empty")

    @commands.command()
    async def clear(self, ctx):
        queue.clear()
        vc = ctx.voice_client
        if vc is not None and vc.is_playing():
            vc.stop()
            await ctx.send("Clearing queue")

    @commands.command()
    async def shuffle(self, ctx):
        global queue
        if queue:
            random.shuffle(queue)
            msg = "Queue shuffled.\n"
            msg += await self.generateQueue(limit=5)
            await ctx.send(msg)
        else:
            await ctx.send("Queue is empty, nothing to shuffle")

    @commands.command()
    async def skip(self, ctx):

        vc = ctx.voice_client
        if vc is not None and vc.is_playing():
            vc.stop()
            await ctx.send("Skipped current track.")
        else:
            await ctx.send("Nothing to skip")

    async def generateQueue(self, limit=None):
        msg = ""
        for i, url in enumerate(queue[:limit] if limit else queue):
            title = await YouTubeService.get_title(url)
            msg += f"{i + 1}. {title}\n"
        if limit and len(queue) > limit:
            msg += f"...and {len(queue) - limit} more tracks in queue."
        return msg
    

async def setup(bot):
    await bot.add_cog(MusicCog(bot))
