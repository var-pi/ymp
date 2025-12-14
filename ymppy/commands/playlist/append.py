import typer
from ymppy. utils import ls, pick, touch
from ymppy.paths import library_dir, playlist_dir

def append():
    """
    Prompt the user to pick a song from the library and a playlist,
    then append the chosen song name to the selected playlist file.
    """
    song  = pick(ls(library_dir))
    playlist = pick(ls(playlist_dir))
    with touch(playlist_dir / playlist).open("a", encoding="utf-8") as f:
        f.write(f"{song}\n")

    typer.echo(f"Added '{song}' to playlist '{playlist}'.")
