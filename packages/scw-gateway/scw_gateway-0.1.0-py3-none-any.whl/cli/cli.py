import click


@click.group()
def cli():
    pass


@cli.command()
def hello():
    """Says hello"""
    click.secho("Hello")


@cli.command()
def list_routes():
    pass


@cli.command()
def add_route():
    pass


@cli.command()
def delete_route():
    pass
