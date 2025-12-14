import typer
from .play import play
from .append import append

app = typer.Typer()
app.command()(play)
app.command()(append)
