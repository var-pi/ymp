import subprocess
import os
import sys
from pathlib import Path
from ymppy.constants import DELIM

import typer
from ymppy.paths import playlist_dir
from ymppy.constants import MAX_RESULTS

def _fzf(items: list[str], with_nth: str) -> str:
    """Show a list in fzf and return the selected item, or None if cancelled."""
    if not items:
        typer.echo("No items were provided", err=True)
        raise typer.Exit(0)
    args = [
        "fzf",
        "--delimiter", DELIM,
        "--with-nth", with_nth,
    ] 
    proc = subprocess.run(
        args,
        input="\n".join(items),
        text=True,
        capture_output=True
    )
    if proc.returncode != 0:
        typer.echo("Fzf process failed", err=True)
        raise typer.Exit(1)
    result_text = proc.stdout.strip()
    if not result_text:
        raise typer.Exit(0)
    return result_text

def play(path: Path, loop: bool = False) -> None:
    if not path.exists():
        typer.echo(f"File not found: {path}", err=True)
        raise typer.Exit(1)
    proc = subprocess.Popen([
        "ffplay",
        "-nodisp",
        "-autoexit",
        "-loglevel", "quiet",
        "-loop", f"{0 if loop else 1}", str(path)])
    try:
        proc.wait()
    except KeyboardInterrupt:
        proc.terminate()
        proc.wait()
        print("\nPlayback interrupted.")

def ls(dir: Path) -> list[str]:
    return [f.name for f in dir.iterdir() if f.is_file()] if dir.exists() else []

def cat(file: Path) -> list[str]:
    lines = [line.strip() for line in file.read_text().splitlines() if line.strip()]
    return lines

def rm(path: Path) -> None:
    try:
        os.remove(path)
        typer.echo(f"Deleted: {path}")
    except FileNotFoundError:
        typer.echo(f"File not found: {path}", err=True)
        raise typer.Exit(code=1)
    except PermissionError:
        typer.echo(f"Permission denied: {path}", err=True)
        raise typer.Exit(code=1)
    except OSError as exc:
        typer.echo(f"Error deleting file: {exc}", err=True)
        raise typer.Exit(code=1)

def yt_dlp(args: list[str], logs: bool = False) -> subprocess.CompletedProcess:
    """Execute yt‑dlp with the given arguments, raising on failure."""
    output: list[str] = []
    proc = None

    try:
        proc = subprocess.Popen(
            ["yt-dlp", *args],
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            bufsize=1,
            text=True,
        )

        assert proc.stdout is not None
        for line in proc.stdout:
            if logs:
                sys.stdout.write(line)
            output.append(line)

        returncode = proc.wait()
    except:
        if proc is not None:
            proc.terminate()
            proc.wait()
        print("\nDownload interrupted.")
        raise typer.Exit(1)

    stdout = "".join(output)

    if returncode != 0:
        typer.echo(f"yt-dlp failed:\n{stdout}", err=True)
        raise typer.Exit(1)

    return subprocess.CompletedProcess(
        args=["yt-dlp", *args],
        returncode=returncode,
        stdout=stdout,
        stderr=None,
    )

def pick(lines: list[str], with_nth: str = "1..") -> str:
    """Delegate to the external fzf UI and return the chosen line."""
    return _fzf(lines, with_nth)

def mkdirp(dir: Path) -> Path:
    """
    Create *dir_path* (and any missing parents) if it does not exist,
    then return the same Path object.

    Equivalent to the shell command `mkdir -p <dir_path>`.
    """
    dir.mkdir(parents=True, exist_ok=True)
    return dir

def touch(path: Path) -> Path:
    path.touch(exist_ok=True)
    return path

def prompt(message: str) -> str:
    """
    Minimal wrapper around ``input`` that writes *message* to stdout
    without adding an extra newline (like the built‑in ``input`` does).

    Returns the raw string entered by the user (including any leading
    or trailing whitespace – callers can ``strip()`` if they wish).
    """
    # ``print`` with ``end=''`` keeps the cursor on the same line.
    print(message, end="", flush=True)
    return input()

def basename(title: str) -> str:
    return title.split(".")[1]

def save(path: Path, lines: list[str]) -> None:
    """Overwrite the file."""
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")

def append(path: Path, line: str):
    path.open("a", encoding="utf-8").write(line + "\n")

def unlink(title: str):
    """Remove a song from all the playlists."""
    for playlist_title in ls(playlist_dir):
        playlist_path = playlist_dir / playlist_title
        lines = cat(playlist_path)
        updated_lines = [line for line in lines if line.strip() != title]
        if len(lines) != len(updated_lines):
            save(playlist_path, updated_lines)

def url():
    """Query a user and provide an appropriate URL."""
    query = prompt("Query: ")
    proc = yt_dlp([
        f"ytsearch{MAX_RESULTS}:{query}",
        "--flat-playlist",
        "--print", f"%(id)s{DELIM}%(duration>%H:%M:%S)s\t%(title)s",
    ])

    # with_nth="2.." to not show video id in picker
    _id = pick(proc.stdout.splitlines(), with_nth="2..").split(DELIM, 1)[0]
    return f"https://www.youtube.com/watch?v={_id}"
