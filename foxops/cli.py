import argparse
import logging

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

args = parser.parse_args()

print(args.server)
