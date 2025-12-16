import os

import typer
from ymppy.utils import pick, ls
from ymppy.paths import playlist_dir

def delete():
    """Delete a playlist."""
    playlist_title = pick(ls(playlist_dir))
    os.remove(playlist_dir / playlist_title)
    typer.echo(f"Playlist {playlist_title} has been deleted")
