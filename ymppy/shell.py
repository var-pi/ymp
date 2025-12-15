import cmd
import shlex
import subprocess
from . import app

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

    def do_exit(self, arg: str) -> bool:
        """Exit ymp"""
        return True

    def do_quit(self, arg: str) -> bool:
        return True
