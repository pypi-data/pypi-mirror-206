import click
from rich.console import Console
from rich.table import Table

from bow.config import templates


@click.command()
def list():
    """List of all available templates."""
    console = Console()
    table = Table(title="All available templates")

    table.add_column("Name")
    table.add_column("Requires")
    table.add_column("URL")

    for ent in templates:
        temp = templates[ent]
        requires = ", ".join(temp["requires"])
        table.add_row(ent, requires, temp["url"])

    console = Console()
    console.print(table)