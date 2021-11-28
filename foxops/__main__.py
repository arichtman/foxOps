import click
import os

from foxops.config import Config

plugin_folder = os.path.join(os.path.dirname(__file__), "commands")


class MyCLI(click.MultiCommand):
    def list_commands(self, ctx):
        rv = []
        for filename in os.listdir(plugin_folder):
            if filename.endswith(".py") and filename != "__init__.py":
                rv.append(filename[:-3])
        rv.sort()
        return rv

    def get_command(self, ctx, name):
        ns = {}
        fn = os.path.join(plugin_folder, name + ".py")
        with open(fn) as f:
            code = compile(f.read(), fn, "exec")
            eval(code, ns, ns)
        return ns["cli"]


@click.group(cls=MyCLI, help="foxOps: declarative config for Gitlab")
@click.pass_context
@click.option(
    "--base-url",
    "-u",
    "_base_url",
    default="https://gitlab.com",
    type=str,
    help="Base URL of the Gitlab server",
)
# This insists on being placed after the first command, ideally it could be put anywhere
@click.option("--debug", "-d", "_debug", is_flag=True, help="Toggles debug level output")
def cli(ctx, _debug, _base_url):
    print(_debug)
    print(_base_url)
    ctx.obj = Config(_base_url, _debug)


if __name__ == "__main__":
    cli(auto_envvar_prefix="FXO")
