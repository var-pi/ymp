from ymppy.utils import fzf_select, files
from ymppy import utils
from ymppy.paths import library_dir
import os
import typer

def remove():
    """Remove a song from library."""
    selected = fzf_select(files(library_dir))
    utils.remove(library_dir / selected)
