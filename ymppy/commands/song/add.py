from pathlib import Path
import subprocess
from ymppy.paths import library_dir
from ymppy.utils import fzf
import typer

def add(query: str):
    max_results = 10
    args = [
        "yt-dlp",
        f"ytsearch{max_results}:{query}",
        "--flat-playlist",
        "--print", "%(id)s %(title)s",
    ]

    result = subprocess.run(
        args,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    result = fzf(result.stdout.splitlines())
    if not result:
        typer.echo("Selection failed.", err=True)
        raise typer.Exit(1)
    id, _ = result.split(" ", 1)

    url = f"https://www.youtube.com/watch?v={id}"
    library_dir.mkdir(parents=True, exist_ok=True)
    subprocess.run([
        "yt-dlp",
        "-x",
        "--no-playlist",
        "-o", f"{library_dir}/%(title)s.%(ext)s",
        "--audio-format", "opus",
        url
    ])

