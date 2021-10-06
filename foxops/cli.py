#!/usr/bin/env python
import argparse
import gitlab
from pprint import pprint

parser = argparse.ArgumentParser(
    description="Push and pull declarative configuration of GitLab applications and repositories",
    add_help=True,
    allow_abbrev=True,
)
parser.add_argument(
    "-s",
    "--server",
    help="server you want to interact with",
    type=str,
    default="https://gitlab.com",
)

parser.add_argument(
    "-t",
    "--token",
    help="api token",
    type=str,
    required=True,
)


def main() -> None:
    args = parser.parse_args()

    # For now, we'll handle this manually. #7 is the start of the thread to improve this
    if args.token.startswith("@"):
        with open(args.token[1:]) as file:
            args.token = file.read()

    gl = gitlab.Gitlab(args.server, private_token=args.token)
    gl.auth()
    project = gl.projects.get(5064907)
    print("done")
