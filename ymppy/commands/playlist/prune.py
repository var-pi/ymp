import typer
from ymppy.utils import pick, ls, basename, cat, save
from ymppy.paths import playlist_dir, library_dir

def prune() -> None:
    """Interactively remove a song from a chosen playlist."""
    playlist_title = pick(ls(playlist_dir))
    playlist_path = playlist_dir / playlist_title
    
    playlist_songs = cat(playlist_path)

    song_title  = pick(playlist_songs, with_nth="2..-2")

    playlist_songs.remove(song_title)
    save(playlist_path, playlist_songs)

    typer.echo(f"Removed '{basename(song_title)}' from {playlist_title}")
