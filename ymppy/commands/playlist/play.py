import random

import typer
from ymppy.utils import pick, ls, cat, play as _play
from ymppy.paths import playlist_dir, library_dir

def play(loop: bool = True, shuffle: bool = True):
    """Play a playlist."""
    songs = cat(playlist_dir / pick(ls(playlist_dir)))
    while True:
        if shuffle:
            random.shuffle(songs)
        for song in songs:
            _play(library_dir / song, loop)
        if not loop:
            break
