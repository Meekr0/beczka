from abc import ABC, abstractmethod


class BaseService(ABC):
    """Abstract base class for music services."""

    @staticmethod
    @abstractmethod
    async def download_audio(url: str) -> bool:
        """Download audio from the given URL.
        
        Args:
            url: The URL to download audio from.
            
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

