#!/usr/bin/env python

import os
import subprocess
from pathlib import Path
import sys
import typer

app = typer.Typer()

@app.command()
def play(loop: bool = False):
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
        "-loop",
        f"{0 if loop else 1}",
        str(song_path),
    ])

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
