#!/usr/bin/env python

import os
import subprocess
from pathlib import Path
import sys
import typer

app = typer.Typer()

def _play_song(loop: bool):
    library_dir = Path.home() / ".ymp-store" / "library"

    if not library_dir.exists():
        typer.echo(f"Library directory does not exist: {library_dir}", err=True)
        raise typer.Exit(1)

    # Get list of files in the library directory
    try:
        files = [f.name for f in library_dir.iterdir() if f.is_file()]
    except PermissionError:
        typer.echo(f"Permission denied accessing: {library_dir}", err=True)
        raise typer.Exit(1)

    if not files:
        typer.echo("No files found in the library directory.", err=True)
        return

    # Use fzf to select a file
    result = subprocess.run(
        ["fzf"],
        input="\n".join(files),
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        # User cancelled selection
        raise typer.Exit(0)

    selected_file = result.stdout.strip()
    song_path = library_dir / selected_file

    if not song_path.exists():
        typer.echo(f"Selected file does not exist: {song_path}", err=True)
        return

    # Play the selected file with ffplay
    subprocess.run([
        "ffplay",
        "-nodisp",
        "-autoexit",
        "-loop",
        f"{0 if loop else 1}",
        str(song_path),
    ])  

def _play_playlist(loop: bool):
    playlist_dir = Path.home() / ".ymp-store" / "playlists"
    library_dir = Path.home() / ".ymp-store" / "library"

    if not playlist_dir.exists():
        typer.echo(f"No playlists found. Directory does not exist: {playlist_dir}", err=True)
        raise typer.Exit(1)

    playlists = [f.name for f in playlist_dir.iterdir() if f.is_file()]
    if not playlists:
        typer.echo("No playlists found.", err=True)
        raise typer.Exit(0)

    # Choose playlist via fzf
    result = subprocess.run(
        ["fzf"],
        input="\n".join(playlists),
        text=True,
        capture_output=True
    )
    if result.returncode != 0:
        # User cancelled selection
        raise typer.Exit(0)

    selected_playlist = result.stdout.strip()
    playlist_file = playlist_dir / selected_playlist

    # Read songs from the playlist
    songs = [line.strip() for line in playlist_file.read_text().splitlines() if line.strip()]
    if not songs:
        typer.echo("Playlist is empty.", err=True)
        raise typer.Exit(0)

    # Play songs in order, loop if requested
    while True:
        for song_name in songs:
            song_path = library_dir / song_name
            if song_path.exists():
                subprocess.run([
                    "ffplay",
                    "-nodisp",
                    "-autoexit",
                    str(song_path)
                ])
            else:
                typer.echo(f"Song not found: {song_name}", err=True)
        if not loop:
            break

@app.command()
def play(loop: bool = False, playlist: bool = False):
    _play_playlist(loop) if playlist else _play_song(loop)

@app.command()
def download(url: str):
    library_dir = Path.home() / ".ymp-store" / "library"
    library_dir.mkdir(parents=True, exist_ok=True)

    # Run yt-dlp command
    cmd = [
        "yt-dlp",
        "-x",
        "--no-playlist",
        "-o", f"{library_dir}/%(title)s.%(ext)s",
        "--audio-format", "opus",
        url
    ]

    subprocess.run(cmd)

if __name__ == "__main__":
    sys.argv[0] = "ymp"
    app()
