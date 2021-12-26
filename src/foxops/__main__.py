from foxops.cli import cli


def main() -> None:
    cli(auto_envvar_prefix="FXO")


if __name__ == "__main__":
    main()
