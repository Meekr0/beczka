from pytubefix import YouTube

from services.base_service import BaseService


class YouTubeService(BaseService):
    """YouTube implementation of the music service."""

    @staticmethod
    async def download_audio(url: str, output_path: str) -> bool:
        """Download audio from YouTube URL to the specified path."""
        try:
            import os
            dir_path = os.path.dirname(output_path)
            file_name = os.path.basename(output_path)
            yt = YouTube(url)
            video = yt.streams.filter(only_audio=True).first()
            video.download(output_path=dir_path, filename=file_name)
            return True
        except Exception as e:
            print(f'Error: {str(e)}')
            return False

    @staticmethod
    async def get_title(url: str) -> str:
        """Get the title of the YouTube video."""
        try:
            yt = YouTube(url)
            return yt.title
        except Exception as e:
            print(f'Error: {str(e)}')
            return "Something went wrong"