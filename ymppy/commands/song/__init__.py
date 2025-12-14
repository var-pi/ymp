import typer
from .play import play
from .add import add
from .remove import remove

app = typer.Typer()
app.command()(play)
app.command()(add)
app.command()(remove)
