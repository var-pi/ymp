import typer
from .play import play
from .append import append
from .new import new

app = typer.Typer()
app.command()(play)
app.command()(append)
app.command()(new)
