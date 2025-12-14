import subprocess
import os
from pathlib import Path

import typer

def _fzf(items: list[str], start_at: int) -> str:
    """Show a list in fzf and return the selected item, or None if cancelled."""
    if not items:
        return None
    args = [
        "fzf",
        "--with-nth", f"{start_at}.."
    ] 
    result = subprocess.run(
        args,
        input="\n".join(items),
        text=True,
        capture_output=True
    )
    if result.returncode != 0:
        return None
    result_text = result.stdout.strip()
    if not result_text:
        raise typer.Exit(0)
    return result_text

def play(path: Path, loop: bool = False) -> None:
    if path.exists():
        subprocess.run(["ffplay", "-nodisp", "-autoexit", "-loop", f"{0 if loop else 1}", str(path)])
    else:
        typer.echo(f"File not found: {path}", err=True)
        raise typer.Exit(1)

def ls(dir: Path) -> list[str]:
    return [f.name for f in dir.iterdir() if f.is_file()] if dir.exists() else []

def cat(file: Path) -> list[str]:
    lines = [line.strip() for line in file.read_text().splitlines() if line.strip()]
    if not lines:
        typer.echo("File is empty.", err=True)
        raise typer.Exit(0)
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

def yt_dlp(args: list[str]) -> subprocess.CompletedProcess:
    """Execute yt‑dlp with the given arguments, raising on failure."""
    proc = subprocess.run(
        ["yt-dlp", *args],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )

    if proc.returncode != 0:
        typer.echo(f"yt-dlp search failed: {proc.stderr}", err=True)
        raise typer.Exit(1)

    return proc

def pick(lines: list[str], start_at: int = 1) -> str:
    """Delegate to the external fzf UI and return the chosen line."""
    return _fzf(lines, start_at=start_at)

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
