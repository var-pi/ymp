import typer
from .play import play
from .new import new
from .delete import delete
from .stream import stream

app = typer.Typer()
app.command()(play)
app.command()(new)
app.command()(delete)
app.command()(stream)
