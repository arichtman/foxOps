import click


@click.group()
@click.pass_obj
@click.option("--id", "-i", "_id", type=int, prompt="Project id number")
def cli(config, _id):
    """
    Subcommand for interacting with groups
    """
    if config.debug:
        print(config)
    print("common for all group")


@cli.command("get")
def get():
    """
    Command for retrieving a group
    """
    _id = None
    print(f"getting group {_id}")


# @click.group('group')
# def gitlab_group():
#     pass

# @gitlab_group.command('get')
# def get_gitlab_group():
#     print('getting gitlab group')
