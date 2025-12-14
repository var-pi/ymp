from ymppy.paths import base_dir, library_dir, playlist_dir
from ymppy.utils import pick, ls, play as _play

def play(loop: bool = False):
    """Play a single song."""
    _play(library_dir / pick(ls(library_dir)), loop=loop) 
