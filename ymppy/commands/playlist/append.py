import typer
from ymppy. utils import ls, pick, touch, append as _append, cat
from ymppy.paths import library_dir, playlist_dir

def append():
    """
    Prompt the user to pick a playlist and a song from the library,
    then append the chosen song name to the selected playlist file.
    """
    playlist_title = pick(ls(playlist_dir))
    playlist_path = playlist_dir / playlist_title
    songs_not_in_playlist = [s for s in ls(library_dir) if s not in cat(playlist_path)]
    song_title = pick(songs_not_in_playlist, with_nth="2..2")
    _append(playlist_path, song_title)

    typer.echo(f"Added '{song_title}' to playlist '{playlist_title}'.")
