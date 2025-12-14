from ymppy.utils import prompt, touch
from ymppy.paths import playlist_dir

def new() -> None:
    """
    Prompt the user for a new playlist name and create an empty file
    in ``playlist_dir``. If a playlist with the same name already exists,
    an error is raised.
    """
    title = ""
    while not title:
        title = prompt("New playlist name: ").strip()
    touch(playlist_dir / f"{title}.m3e")
    print(f"Playlist \"{title}\" created.")
