import typer
from ymppy.utils import pick, ls, cat, play as _play
from ymppy.paths import playlist_dir, library_dir

def play(loop: bool = False):
    """Play a playlist."""
    songs = cat(playlist_dir / pick(ls(playlist_dir)))
    while True:
        for song in songs:
            _play(library_dir / song)
        if not loop:
            break
