#!/usr/bin/env python

import subprocess
from pathlib import Path
import sys
import typer

app = typer.Typer()

@app.command()
def play(loop: bool = False, playlist: bool = False):
    """Play a single song or a playlist."""
    base_dir = Path.home() / ".ymp-store"
    library_dir = base_dir / "library"

    if playlist:
        playlist_dir = base_dir / "playlists"
        playlists = [f.name for f in playlist_dir.iterdir() if f.is_file()] if playlist_dir.exists() else []
        selected = _fzf_select(playlists)
        if not selected:
            raise typer.Exit(0)
        songs = [line.strip() for line in (playlist_dir / selected).read_text().splitlines() if line.strip()]
        if not songs:
            typer.echo("Playlist is empty.", err=True)
            raise typer.Exit(0)
        while True:
            for song in songs:
                _play_file(library_dir / song)
            if not loop:
                break
    else:
        files = [f.name for f in library_dir.iterdir() if f.is_file()] if library_dir.exists() else []
        selected = _fzf_select(files)
        if not selected:
            raise typer.Exit(0)
        _play_file(library_dir / selected, loop=loop)

@app.command()
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

if __name__ == "__main__":
    sys.argv[0] = "ymp"
    app()
