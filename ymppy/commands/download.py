from pathlib import Path
import subprocess

def download(url: str):
    """Download a song to the library using yt-dlp."""
    library_dir = Path.home() / ".ymp-store" / "library"
    library_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "yt-dlp",
        "-x",
        "--no-playlist",
        "-o", f"{library_dir}/%(title)s.%(ext)s",
        "--audio-format", "opus",
        url
    ])
