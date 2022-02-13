import logging

import click

logger = logging.getLogger(__name__)


@click.group("group", help="set of commands to work with groups")
@click.pass_obj
def cli(config):
    """Subcommand for interacting with groups"""
    # This function runs for all group subcommands
    logger.debug(config)


group_id_argument = click.argument(
    "id",
    type=int,
)


@cli.command("get")
@group_id_argument
def get(id):
    """Command for retrieving a group"""
    logger.info(f"getting group {id}")


@cli.command("delete")
@group_id_argument
def delete(id):
    """Command for deleting a group"""
    logger.info(f"deleting group {id}")
