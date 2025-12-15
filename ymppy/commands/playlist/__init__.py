import typer
from .play import play
from .append import append
from .new import new
from .prune import prune
from .delete import delete

app = typer.Typer()
app.command()(play)
app.command()(append)
app.command()(new)
app.command()(prune)
app.command()(delete)
