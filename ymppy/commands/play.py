from pathlib import Path
from ymppy.utils import play_file, fzf_select

def play(loop: bool = False, playlist: bool = False):
    """Play a single song or a playlist."""
    base_dir = Path.home() / ".ymp-store"
    library_dir = base_dir / "library"

    if playlist:
        playlist_dir = base_dir / "playlists"
        playlists = [f.name for f in playlist_dir.iterdir() if f.is_file()] if playlist_dir.exists() else []
        selected = fzf_select(playlists)
        if not selected:
            raise typer.Exit(0)
        songs = [line.strip() for line in (playlist_dir / selected).read_text().splitlines() if line.strip()]
        if not songs:
            typer.echo("Playlist is empty.", err=True)
            raise typer.Exit(0)
        while True:
            for song in songs:
                play_file(library_dir / song)
            if not loop:
                break
    else:
        files = [f.name for f in library_dir.iterdir() if f.is_file()] if library_dir.exists() else []
        selected = fzf_select(files)
        if not selected:
            raise typer.Exit(0)
        play_file(library_dir / selected, loop=loop)
