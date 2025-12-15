import typer
from ymppy.utils import pick, ls, basename, cat, save
from ymppy.paths import playlist_dir, library_dir

def prune() -> None:
    """Interactively remove a song from a chosen playlist."""
    playlist_title = pick(ls(playlist_dir))
    playlist_path = playlist_dir / playlist_title
    
    playlist_songs = cat(playlist_path)

    song  = pick(playlist_songs)

    playlist_songs.remove(song)
    save(playlist_path, playlist_songs)

    typer.echo(f"Removed '{basename(song)}' from {basename(playlist_title)}")
