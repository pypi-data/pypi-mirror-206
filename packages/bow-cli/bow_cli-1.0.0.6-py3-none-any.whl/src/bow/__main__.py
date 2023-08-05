import json
import os
import stat
import sys

import click
import git
import mcfc
import requests
from rich.console import Console
from rich.table import Table

from .__about__ import __version__

curr_path = sys.path[0]
tempfile = curr_path + "/templates.json"

with open(tempfile, "r+") as fp:
    templates = json.load(fp)
    fp.close()


def success(*objects):
    mcfc.echo("&a✔&r", *objects, "\n")

def info(*objects):
    mcfc.echo("&bℹ&r", *objects, "\n")

def error(*objects):
    mcfc.echo("&c✖&r", *objects, "\n")

def warn(*objects):
    mcfc.echo("&e⚠&r", *objects, "\n")


def rmtree(top):
    for root, dirs, files in os.walk(top, topdown=False):
        for name in files:
            filename = os.path.join(root, name)
            os.chmod(filename, stat.S_IWUSR)
            os.remove(filename)
        for name in dirs:
            os.rmdir(os.path.join(root, name))
    os.rmdir(top)


def check_url_validate(url):
    try:
        code = requests.get(url).status_code
        if code in range(400, 500):
            return warn("An client error in getting template occured, status code: ", code)
        elif code in range(500, 600):
            return warn("An server error in getting template occured, status code: ", code)
    except requests.exceptions.MissingSchema:
        warn("The URL is not valid, it cause the template not to work.")
    except requests.exceptions.ConnectionError:
        warn("Failed to establish a new connection. URL checking not passed.")
        
        
def extract_repo_name(url):
    return url.rstrip('.git').split('/')[-1]


def validate_git_repo(url):
    if url.startswith("https://") or url.startswith("http://"):
        if url.endswith(".git"):
            return True
        else:
            return validate_git_repo(url + ".git")
    else:
        return False


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


@click.command()
@click.argument("template")
@click.option("-n", "--name", "name_", help="The name of the project, which will be specified in generated files (README and others).")
@click.option("-d", "--dir", "dir_", help="Path where project will be generated in.")
@click.option("-r", "--remove-git", help="Removes /.git directory.", default=False, show_default=False, is_flag=True)
def g(template, name_, dir_, remove_git):
    """Generate projects using built-in, custom templates or git repos."""
    try:
        name = name_ if name_ else template

        if validate_git_repo(template):
            info("Checking URL validate ...")
            check_url_validate(template)
            name = name_ if name_ else extract_repo_name(template)
            url = template
        else:
            temp = templates[template]
            url = temp["url"]
        
        dist = os.getcwd() + "\\" + name
        
        if dir_:
            dirc = os.getcwd() + dir_.replace("/", "\\")
            dist = dirc + "\\" + name
        
        info(f"Creating folder '{name}' ...")
        os.mkdir(dist)
        
        info(f"Cloning from {url} ...")
        git.Repo.clone_from(url, dist)
        
        if remove_git:
            info("Removing .git\ ...")
            rmtree(dist + "\.git")

        success("Project successfully created.")
    except FileExistsError:
        error("Folder with this name already exists.")
    except FileNotFoundError:
        error(f"Cannot find the path: {dirc}.")
    except KeyError:
        error("Template not found.")


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
    
    
bow.add_command(g)
bow.add_command(list)
bow.add_command(remove)
bow.add_command(add)


def main():
    return bow(prog_name='bow', windows_expand_args=False)


if __name__ == '__main__':
    sys.exit(main())