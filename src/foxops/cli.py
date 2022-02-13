import logging
import os

import click
from dotenv import load_dotenv
from foxops.config import Config
from foxops.foxops import FoxOps

plugin_folder = os.path.join(os.path.dirname(__file__), "commands")
logger = logging.getLogger(__name__)
load_dotenv()

env_access_token = os.getenv("FXO_ACCESS_TOKEN")
env_base_url = os.getenv("FXO_BASE_URL")


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
            # I'm unsure why this is split into 2 phases and not just one `exec()` call...
            code = compile(f.read(), fn, "exec")  # nosemgrep
            # can't use literal_eval since we need function type objects
            eval(code, ns, ns)  # nosemgrep
        return ns["cli"]


@click.group(name="cli", cls=CommandLineApp, help="foxOps: declarative config for Gitlab")
@click.pass_context
@click.option(
    "--base-url",
    "-u",
    default="https://gitlab.com" if not env_base_url else env_base_url,
    type=str,
    help="Base URL of the Gitlab server",
)
# This insists on being placed after the first command, ideally it could be put anywhere
@click.option("--debug", "-d", is_flag=True, help="Toggles debug level output")
@click.option("--access-token", "-t", required=(not env_access_token), help="GitLab personal access token")
# NB: locate context object type
def cli(ctx, debug: bool, base_url: str, access_token: str) -> None:
    """Actual root function that handles the cli"""

    if access_token is None:
        access_token = env_access_token

    if debug:
        logging.basicConfig(level=logging.DEBUG)
        logger.debug(debug)
        logger.debug(base_url)
        logger.debug(access_token)
        from pprint import pprint

        # pprint(os.environ) still ugly
        env = {key: val for key, val in os.environ.items() if key.startswith("FXO")}
        pprint(env)

    else:
        logging.basicConfig(level=logging.INFO)

    Config(base_url=base_url, access_token=access_token)

    ctx.obj = FoxOps(base_url=base_url, access_token=access_token)
