import typer
from ymppy. utils import ls, pick, touch, append as _append
from ymppy.paths import library_dir, playlist_dir

def append():
    """
    Prompt the user to pick a playlist and a song from the library,
    then append the chosen song name to the selected playlist file.
    """
    playlist = pick(ls(playlist_dir))
    song  = pick(ls(library_dir), with_nth="2..2")
    _append(playlist_dir / playlist, song)

    typer.echo(f"Added '{song}' to playlist '{playlist}'.")
