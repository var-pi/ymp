import typer
from ymppy.commands.playlist.play import play

app = typer.Typer()
app.command()(play)
