import json

import click

from bow.cli.config import tempfile
from bow.cli.utils.logger import info, success


@click.command()
@click.argument("name")
def remove(name):
    """Removes a template from templates file."""
    with open(tempfile, "r") as f:
        info("Reading templates file ...")
        data = json.load(f)
        f.close()
    
    del data[name]
    
    with open(tempfile, "w") as f:
        json.dump(data, f, indent=4)
        f.close()
        success("Template successfully removed.")