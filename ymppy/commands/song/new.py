from pathlib import Path
import subprocess

import typer
from ymppy.paths import library_dir
from ymppy.utils import pick, yt_dlp, mkdirp, prompt
from ymppy.constants import MAX_RESULTS, DELIM

def new() -> None:
    query = prompt("Query: ")
    """Search YouTube, let the user pick a video, and download its audio as Opus."""
    proc = yt_dlp([
        f"ytsearch{MAX_RESULTS}:{query}",
        "--flat-playlist",
        "--print", f"%(id)s{DELIM}%(title)s",
    ])

    # with_nth="2.." to not show video id in picker
    _id, title = pick(proc.stdout.splitlines(), with_nth="2..").split(DELIM, 1)
    url = f"https://www.youtube.com/watch?v={_id}"
    output_path = mkdirp(library_dir) / f"%(id)s{DELIM}%(title)s{DELIM}%(ext)s"
    yt_dlp([
        "-x",
        "--no-playlist",
        "-o", str(output_path),
        "--audio-format", "opus",
        url
    ])

    typer.echo(f"\"{title}\" has been downloaded.")
