import typer
from ymppy. utils import ls, pick, touch, append as _append, cat, basename
from ymppy.paths import library_dir, playlist_dir

def append():
    """
    Prompt the user to pick a playlist and a song from the library,
    then append the chosen song name to the selected playlist file.
    """
    playlisted_songs = [s for pl in ls(playlist_dir) for s in cat(playlist_dir / pl)]

    #unplaylisted_songs = [s for s in ls(library_dir) if s not in playlisted_songs]
    unplaylisted_songs = list(set(ls(library_dir))-set(playlisted_songs))
    song_title = pick(unplaylisted_songs, with_nth="2..2")
    playlist_title = pick(ls(playlist_dir))
    _append(playlist_dir / playlist_title, song_title)

    typer.echo(f"Added '{basename(song_title)}' to playlist '{playlist_title}'.")
