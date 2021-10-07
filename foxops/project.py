import typer
from pprint import pprint
from foxops.configuration import configuration
from gitlab import v4
from json import dumps

app = typer.Typer()


@app.command()
def get(handle: str) -> v4.objects.projects.Project:
    gl = configuration.get("gitlab_object")
    # This search is too rudimentary #17
    all_owned_projects = gl.projects.list(search=handle, owned=True)
    if len(all_owned_projects) > 1:
        raise Exception("Too many project results located, unable to resolve ambiguity")
    elif len(all_owned_projects) == 0:
        raise Exception("No project results located")
    project = all_owned_projects[0]
    typer.echo(dumps(project.attributes, indent=4))


@app.command()
def set(handle: str, property: str, value: str):
    typer.echo(f"Setting project {handle} property {property} to {value}")
