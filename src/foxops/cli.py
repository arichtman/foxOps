# type: ignore
import logging
import os

import click
from foxops.config import Config
from foxops.foxops import FoxOps

plugin_folder = os.path.join(os.path.dirname(__file__), "commands")
logger = logging.getLogger(__name__)


class CommandLineApp(click.MultiCommand):
    """The root class that Click uses"""

    def list_commands(self, ctx):
        """Locates all valid subcommand modules"""
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        """Retrieves all found subcommands"""
        ns = {}
        fn = os.path.join(plugin_folder, name + ".py")
        if not os.path.exists(fn):
            raise ValueError("Command passed is not supported by this package")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
        return ns["cli"]


@click.group(name="cli", cls=CommandLineApp, help="foxOps: declarative config for Gitlab")
@click.pass_context
@click.option(
    "--base-url",
    "-u",
    default="https://gitlab.com",
    type=str,
    help="Base URL of the Gitlab server",
)
# This insists on being placed after the first command, ideally it could be put anywhere
@click.option("--debug", "-d", is_flag=True, help="Toggles debug level output")
@click.option("--access-token")
# TODO: locate context object type
def cli(ctx, debug: bool, base_url: str, access_token: str) -> None:
    """Actual root function that handles the cli"""
    if debug:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    logger.debug(debug)
    logger.debug(base_url)
    logger.debug(access_token)
    # Something's not right here, we shouldn't be
    Config(base_url=base_url, debug=debug, access_token=access_token)
    # The foxops object could be adjusted to take the config object but something about that coupling feels bad
    # I could try some abstract class/interface but that seems overkill for this? Maybe if other parts start
    # using the config object...
    ctx.obj = FoxOps(base_url=base_url, access_token=access_token)
