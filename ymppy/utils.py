import subprocess
import os
import typer
from pathlib import Path

def fzf(items: list[str]) -> str | None:
    """Show a list in fzf and return the selected item, or None if cancelled."""
    if not items:
        return None
    result = subprocess.run(["fzf"], input="\n".join(items), text=True, capture_output=True)
    if result.returncode != 0:
        return None
    result_text = result.stdout.strip()
    if not result_text:
        raise typer.Exit(0)
    return result_text

def play(path: Path, loop: bool = False):
    if path.exists():
        subprocess.run(["ffplay", "-nodisp", "-autoexit", "-loop", f"{0 if loop else 1}", str(path)])
    else:
        typer.echo(f"File not found: {path}", err=True)

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
