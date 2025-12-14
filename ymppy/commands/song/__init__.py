import typer
from .play import play
from .add import add
from .delete import delete

app = typer.Typer()
app.command()(play)
app.command()(add)
app.command()(delete)
