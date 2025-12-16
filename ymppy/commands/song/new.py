from pathlib import Path
import subprocess

from ymppy.paths import library_dir
from ymppy.utils import pick, yt_dlp, mkdirp, prompt, url
from ymppy.constants import MAX_RESULTS, DELIM

def new() -> None:
    """Search YouTube, let the user pick a video, and download its audio as Opus."""
    output_path = mkdirp(library_dir) / f"%(id)s{DELIM}%(title)s{DELIM}%(ext)s"
    proc = yt_dlp([
        "-x",
        "--no-playlist",
        "-o", str(output_path),
        "--audio-format", "opus",
        url()
    ], True)
