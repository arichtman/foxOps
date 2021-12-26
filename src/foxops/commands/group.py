# from typing_extensions import Required
import logging

import click


@click.group("group", help="set of commands to work with groups")
@click.pass_obj
def cli(config):
    """
    Subcommand for interacting with groups
    """
    # This function runs for all group subcommands
    logging.debug(config)


group_id_argument = click.option(
    "--id",
    "-i",
    "_id",
    required=True,
    type=int,
    help="Integer identifier, the primary key of the group",
)


@cli.command("get")
@group_id_argument
def get(_id):
    """
    Command for retrieving a group
    """
    logging.info(f"getting group {_id}")


@cli.command("delete")
@group_id_argument
def delete(_id):
    """
    Command for deleting a group
    """
    logging.info(f"deleting group {_id}")
