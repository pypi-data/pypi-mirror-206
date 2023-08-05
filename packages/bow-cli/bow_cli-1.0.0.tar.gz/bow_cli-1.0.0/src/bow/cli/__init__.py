import sys

import click
from rich.console import Console

from bow.__about__ import __version__
from bow.cli.commands.add import add
from bow.cli.commands.g import g
from bow.cli.commands.list import list
from bow.cli.commands.remove import remove


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='Bow')
def bow():
    """
    \b
    .______     ______   ____    __    ____ 
    |   _  \   /  __  \  \   \  /  \  /   / 
    |  |_)  | |  |  |  |  \   \/    \/   /  
    |   _  <  |  |  |  |   \            /   
    |  |_)  | |  `--'  |    \    /\    /    
    |______/   \______/      \__/  \__/      
    """
    pass


bow.add_command(g)
bow.add_command(list)
bow.add_command(remove)
bow.add_command(add)


def main():
    try:
        return bow(prog_name='bow', windows_expand_args=False)
    except Exception:
        suppressed_modules = []
        if not getattr(sys, 'frozen', False):
            suppressed_modules.append(click)

        console = Console()
        console.print_exception(suppress=suppressed_modules)
        return 1
