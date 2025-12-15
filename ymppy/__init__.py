from .commands import app
import typer
from .shell import YmpShell

@app.callback(invoke_without_command=True)
def main(ctx: typer.Context) -> None:
    if ctx.invoked_subcommand is None:
        YmpShell().cmdloop()
