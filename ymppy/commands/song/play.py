import typer
from ymppy.paths import base_dir, library_dir, playlist_dir
from ymppy.utils import play_file, fzf_select, files

def play(loop: bool = False):
    """Play a single song."""
    selected = fzf_select(files(library_dir))
    if not selected:
        raise typer.Exit(0)
    play_file(library_dir / selected, loop=loop)
