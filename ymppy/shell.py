from typing import Any
import os
import cmd
import shlex
import subprocess
from . import app
import typer
import re

def parse_zsh_arguments(output: str) -> list[str]:
    """
    Extract completion names from zsh _arguments output.
    """
    # Math all argument names
    return re.findall(r'[^:]"([a-zA-Z]+)"', output)

class YmpShell(cmd.Cmd):
    intro = "Welcome to ymp. Type help or ? to list commands."
    prompt = "ymp> "

    def default(self, line: str) -> None:
        """
        Forward all input to the Typer app.
        """
        argv = shlex.split(line)
        if not argv:
            return

        try:
            app(argv)
        except SystemExit:
            # Typer exits after each command; suppress it
            pass

    def completenames(self, text: str, *ignored: Any) -> list[str]:
        return self.completedefault(text, text, 0, 0)

    def completedefault(self, text, line, begidx, endidx) -> list[str]: # ty: ignore[invalid-method-override]
        try:
            env = dict(os.environ)
            env["_YMP_COMPLETE"] = "complete_zsh"
            env["_TYPER_COMPLETE_ARGS"] = "ymp " + line
            result = subprocess.run(
                ["ymp"], capture_output=True, text=True, env=env
            )
            return parse_zsh_arguments(result.stdout)
        except Exception:
            return []
