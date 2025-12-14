#!/usr/bin/env python3

import sys
import typer
from ymppy.commands import song, playlist

app = typer.Typer()
app.add_typer(song.app, name="song")
app.add_typer(playlist.app, name="playlist")

if __name__ == "__main__":
    app()
