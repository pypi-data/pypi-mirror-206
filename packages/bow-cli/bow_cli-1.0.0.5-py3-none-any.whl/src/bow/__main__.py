import sys

import click

from bow.commands.add import add
from bow.commands.g import g
from bow.commands.list import list
from bow.commands.remove import remove

from .__about__ import __version__


@click.group(context_settings={'help_option_names': ['-h', '--help']}, invoke_without_command=True)
@click.version_option(version=__version__, prog_name='Bow')
def bow():
    """
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
    return bow(prog_name='bow', windows_expand_args=False)


if __name__ == '__main__':
    sys.exit(main())