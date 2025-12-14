from pathlib import Path
import subprocess
from ymppy.paths import library_dir

def add(url: str):
    """Download a song to the library using yt-dlp."""
    library_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "yt-dlp",
        "-x",
        "--no-playlist",
        "-o", f"{library_dir}/%(title)s.%(ext)s",
        "--audio-format", "opus",
        url
    ])
