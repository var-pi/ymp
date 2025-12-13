import subprocess
import typer
from pathlib import Path

def _fzf_select(items: list[str]) -> str | None:
    """Show a list in fzf and return the selected item, or None if cancelled."""
    if not items:
        return None
    result = subprocess.run(["fzf"], input="\n".join(items), text=True, capture_output=True)
    if result.returncode != 0:
        return None
    return result.stdout.strip()

def _play_file(path: Path, loop: bool = False):
    if path.exists():
        subprocess.run(["ffplay", "-nodisp", "-autoexit", "-loop", f"{0 if loop else 1}", str(path)])
    else:
        typer.echo(f"File not found: {path}", err=True)
