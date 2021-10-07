#!/usr/bin/env python
from foxops.configuration import configuration
import typer
import gitlab
from pprint import pprint

import foxops.project
import foxops.group

app = typer.Typer(
    name="foxops",
    help="foxops command line interface for pushing and pulling Gitlab configuration",
    context_settings={"help_option_names": ["-h", "--help", "-?"]},
)
app.add_typer(foxops.project.app, name="project")
app.add_typer(foxops.group.app, name="group")


def main(foo: str = "") -> None:
    app()
