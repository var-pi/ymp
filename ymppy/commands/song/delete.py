from ymppy.utils import pick, ls, rm
from ymppy.paths import library_dir

def delete():
    """Remove a song from library."""
    rm(library_dir / pick(ls(library_dir), with_nth="2..-2"))
