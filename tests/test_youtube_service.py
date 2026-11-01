import asyncio
import os
import shutil
import subprocess
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import Mock

import pytest

from services.youtube import youtube_service


YOUTUBE_TEST_URL = "https://www.youtube.com/watch?v=dQw4w9WgXcQ"
EXPECTED_DURATION_IN_SECONDS = 213


def test_download_audio_saves_stream(monkeypatch, tmp_path):
    audio_bytes = b"test audio data"
    audio_stream = Mock()
    audio_stream.download.side_effect = lambda output_path, filename: Path(output_path, filename).write_bytes(audio_bytes)
    streams = Mock()
    streams.filter.return_value = streams
    streams.first.return_value = audio_stream

    monkeypatch.setattr(
        youtube_service, "YouTube", lambda url: SimpleNamespace(streams=streams)
    )

    output_file = f"{tmp_path}{os.sep}audio.webm"
    assert asyncio.run(youtube_service.YouTubeService.download_audio("https://example.com/video", output_file))
    assert Path(output_file).read_bytes() == audio_bytes


def test_download_audio_from_youtube(monkeypatch, tmp_path):
    url = YOUTUBE_TEST_URL
    if not url:
        pytest.skip("Set YOUTUBE_TEST_URL to run the YouTube integration test")

    ffprobe = shutil.which("ffprobe")
    assert ffprobe, "ffprobe is required for the YouTube integration test (install FFmpeg)"

    output_file = f"{tmp_path}{os.sep}audio.webm"
    audio_path = Path(output_file)

    assert asyncio.run(youtube_service.YouTubeService.download_audio(url, output_file))
    assert audio_path.is_file()
    minimum_size = int(os.getenv("YOUTUBE_TEST_MIN_SIZE_BYTES", "1024"))
    assert audio_path.stat().st_size >= minimum_size

    result = subprocess.run(
        [
            ffprobe,
            "-v",
            "error",
            "-show_entries",
            "format=duration",
            "-of",
            "csv=p=0",
            str(audio_path),
        ],
        check=True,
        capture_output=True,
        text=True,
    )
    duration = float(result.stdout.strip())
    assert duration > 0

    expected_duration = EXPECTED_DURATION_IN_SECONDS
    if expected_duration:
        assert duration == pytest.approx(float(expected_duration), abs=2.0)