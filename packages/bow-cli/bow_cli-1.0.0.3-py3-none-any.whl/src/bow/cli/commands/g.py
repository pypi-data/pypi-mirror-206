import os

import click
import git

from bow.cli.config import templates
from bow.cli.utils.fs import rmtree
from bow.cli.utils.http import (check_url_validate, extract_repo_name,
                            validate_git_repo)
from bow.cli.utils.logger import error, info, success


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
        