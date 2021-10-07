import typer

app = typer.Typer()


@app.command()
def get(handle: str):
    typer.echo(f"Retrieving group {handle}")


@app.command()
def set(handle: str, property: str, value: str):
    typer.echo(f"Setting group {handle} property {property} to {value}")
