import json

import click

from bow.config import tempfile
from bow.utils.http import check_url_validate
from bow.utils.logger import info, success


@click.command()
@click.argument("name")
@click.argument("url")
@click.option("-r", "--require", "req", help="Modules, libraries, SDKs that your template requires.", multiple=True)
@click.option("-U", "--disable-url-checking", "duc", help="Disable URL validation checking.", is_flag=True, default=False, show_default=False)
def add(name, url, req, duc):
    """Add a custom template."""
    if not duc:
        info("Checking URL validate ...")
        check_url_validate(url)
    
    with open(tempfile, "r") as f:
        info("Reading templates file ...")
        data = json.load(f)
        f.close()
    
    data[name] = {
        "url": url,
        "requires": req if req else []
    }
    
    with open(tempfile, "w+") as f:
        json.dump(data, f, indent=4)
        f.close()
        success("Template successfully added.")