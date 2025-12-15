import os

import typer
from ymppy.utils import pick, ls, basename
from ymppy.paths import playlist_dir

def delete():
    playlist_title = pick(ls(playlist_dir))
    os.remove(playlist_dir / playlist_title)
    typer.echo(f"Playlist {basename(playlist_title)} has been deleted")
