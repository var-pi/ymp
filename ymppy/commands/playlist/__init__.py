import typer
from .play import play

app = typer.Typer()
app.command()(play)
