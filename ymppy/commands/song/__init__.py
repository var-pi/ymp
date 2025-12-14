import typer
from ymppy.commands.song.play import play
from ymppy.commands.song.add import add

app = typer.Typer()
app.command()(play)
app.command()(add)
