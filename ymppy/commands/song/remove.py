from ymppy.utils import fzf, ls, rm
from ymppy.paths import library_dir

def remove():
    """Remove a song from library."""
    rm(library_dir / fzf(ls(library_dir)))
