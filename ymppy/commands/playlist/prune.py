import typer
from ymppy.utils import pick, ls
from ymppy.paths import playlist_dir, library_dir

def prune():
    playlist = pick(ls(playlist_dir))

    playlist_songs: list[str]

    with open(playlist_dir / playlist, "r", encoding="utf-8") as f:
        playlist_songs = [line.rstrip("\n") for line in f]

    if not playlist_songs:
        typer.echo(f"Playlist {playlist} is empty.")
        raise typer.Exit(0)

    song  = pick(playlist_songs)

    playlist_songs.remove(song)

    with open(playlist_dir / playlist, "w", encoding="utf-8") as f:
        f.write("\n".join(playlist_songs) + "\n")
    print(f"Removed '{song}' from {playlist}")
