import typer
from ymppy.commands.song.play import play
from ymppy.commands.song.add import add
from ymppy.commands.song.remove import remove

a = 1

app = typer.Typer()
app.command()(play)
app.command()(add)
app.command()(remove)
