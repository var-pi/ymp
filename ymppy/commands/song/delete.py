from ymppy.utils import pick, ls, rm, unlink
from ymppy.paths import library_dir
                    
def delete():
    """Remove a song from library."""
    song_title = pick(ls(library_dir), with_nth="2..-2")
    unlink(song_title)
    rm(library_dir / song_title)
