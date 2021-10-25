import click

@click.command()
@click.option('--string', default='World', help="Who will be greeted")
def cli(string):
    """This script greets you."""
    click.echo(f"Hello, {string}")