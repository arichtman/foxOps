import click
import os

from click.types import StringParamType

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


class Config:
    """
    Structure intended to hold any globally used configuration items
    """

    def __init__(self, base_url="https://gitlab.com", debug=False, access_token=None):
        self.base_url = base_url
        self.debug = debug
        self.access_token = access_token

    # Yuck
    def __str__(self):
        return "\n".join(
            str(item) for item in [self.base_url, self.debug, self.access_token]
        )


@click.group(cls=MyCLI, help="foxOps: declarative config for Gitlab")
@click.pass_context
@click.option(
    "--base-url", "-u", "_base_url", type=str, help="Base URL of the Gitlab server"
)
@click.option("--debug", "-d", "_debug", is_flag=True, help="Toggles debug level output")
def cli(ctx, _debug, _base_url):
    ctx.obj = Config(_base_url, _debug)


if __name__ == "__main__":
    cli()
