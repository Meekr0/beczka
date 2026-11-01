from abc import ABC, abstractmethod
from typing import List


class BaseService(ABC):
    """Abstract base class for music services."""

    @staticmethod
    @abstractmethod
    async def download_audio(url: str, output_path: str) -> bool:
        """Download audio from the given URL to the specified path.
        
        Args:
            url: The URL to download audio from.
            output_path: Path where the audio file should be saved.
            
        Returns:
            bool: True if download succeeded, False otherwise.
        """
        pass

    @staticmethod
    @abstractmethod
    async def get_title(url: str) -> str:
        """Get the title of the media from the given URL.
        
        Args:
            url: The URL to get the title from.
            
        Returns:
            str: The title of the media, or error message if failed.
        """
        pass

    @staticmethod
    @abstractmethod
    async def is_playlist(url: str) -> bool:
        """Check if the given URL is a playlist.
        
        Args:
            url: The URL to check.
            
        Returns:
            bool: True if the URL is a playlist, False otherwise.
        """
        pass

    @staticmethod
    @abstractmethod
    async def get_playlist_urls(url: str) -> List[str]:
        """Get all video URLs from a playlist.
        
        Args:
            url: The playlist URL.
            
        Returns:
            List[str]: List of video URLs in the playlist.
        """
        pass

    @staticmethod
    @abstractmethod
    async def get_playlist_title(url: str) -> str:
        """Get the title of a playlist.
        
        Args:
            url: The playlist URL.
            
        Returns:
            str: The title of the playlist, or error message if failed.
        """
        pass

