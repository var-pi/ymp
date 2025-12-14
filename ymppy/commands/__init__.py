import typer
from . import song, playlist

app = typer.Typer()
app.add_typer(song.app, name="song")
app.add_typer(playlist.app, name="playlist")
