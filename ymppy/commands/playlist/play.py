import typer
from ymppy.utils import fzf_select, files, play_file, lines
from ymppy.paths import playlist_dir, library_dir

def play(loop: bool = False):
    """Play a playlist."""
    selected = fzf_select(files(playlist_dir))
    songs = lines(playlist_dir / selected)
    while True:
        for song in songs:
            play_file(library_dir / song)
        if not loop:
            break
