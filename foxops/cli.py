#!/usr/bin/env python
import click


@click.group()
@click.option("--verbose", "-v", "_verbose", type=bool, help="Toggle debug level output")
@click.option(
    "--config-file",
    "-c",
    "_config_file",
    type=click.File("rb"),
    help="Path to YAML/JSON config file",
)
def cli(_verbose, _config_file) -> None:
    """
    CLI interface for declarative configuration of Gitlab resources
    """
    if _verbose:
        print("****")


@cli.group("group")
def gitlab_group():
    # do anything common to all groups here
    pass


@cli.group("project")
def gitlab_project():
    pass


@gitlab_group.command("get")
@click.option("--id", "-i", "_id", type=int, prompt="Project id number")
def get_gitlab_group(_id):
    print(f"getting group {_id}")
