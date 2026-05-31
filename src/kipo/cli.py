import typer

from kipo.commands.version import version
from kipo.commands.studio import studio

app = typer.Typer()

app.command()(version)
app.command()(studio)