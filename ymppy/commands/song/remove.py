from ymppy.utils import pick, ls, rm
from ymppy.paths import library_dir

def remove():
    """Remove a song from library."""
    rm(library_dir / pick(ls(library_dir)))
