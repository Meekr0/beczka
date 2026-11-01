"""Service detection for music URLs."""

from enum import Enum
from typing import Optional

from services.youtube.youtube_service import YouTubeService


class SupportedService(Enum):
    """Supported music services."""
    YOUTUBE = "youtube"
    # Add more services here when needed: SPOTIFY = "spotify", etc.


# Service class mapping
SERVICE_CLASSES = {
    SupportedService.YOUTUBE: YouTubeService,
    # SupportedService.SPOTIFY: SpotifyService,
}

# URL patterns for each service
SERVICE_URL_PATTERNS = {
    SupportedService.YOUTUBE: ['youtube.com', 'youtu.be', 'youtube-nocookie.com'],
    # SupportedService.SPOTIFY: ['spotify.com', 'open.spotify.com'],
}


def detect_service(url: str) -> Optional[SupportedService]:
    """Detect which service the URL belongs to.
    
    Args:
        url: The URL to check.
        
    Returns:
        SupportedService: The detected service, or None if not supported.
    """
    url_lower = url.lower()
    
    for service, patterns in SERVICE_URL_PATTERNS.items():
        if any(pattern in url_lower for pattern in patterns):
            return service
    
    return None


def get_service_instance(service: SupportedService):
    """Get service instance for the given service enum.
    
    Args:
        service: The SupportedService enum value.
        
    Returns:
        Service instance (e.g., YouTubeService).
    """
    return SERVICE_CLASSES[service]()


def get_supported_services_list() -> str:
    """Get a comma-separated list of supported service names.
    
    Returns:
        str: Comma-separated list of supported services.
    """
    return ", ".join(service.value for service in SupportedService)
