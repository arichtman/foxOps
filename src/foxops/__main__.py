# type: ignore
# I am getting really sick of mypy's sh*t
from foxops.cli import cli


def main() -> None:
    """Indirection to allow for launch of the application"""
    cli(auto_envvar_prefix="FXO")


if __name__ == "__main__":
    main()
