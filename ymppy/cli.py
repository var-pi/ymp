#!/usr/bin/env python3

import sys
import typer
from ymppy.commands.play import play
from ymppy.commands.download import download

app = typer.Typer()
app.command()(play)
app.command()(download)

if __name__ == "__main__":
    app()
