import click


@click.command()
def greet():
    click.echo("hello, world")

@click.command()
@click.option("--count", default=1, help="Number of greetngs.")
@click.option("--name", prompt="your name", help="The person to greet.")
def greet2(count, name):
    """ Simple program that greets Name for a total of Count times"""
    for _ in range(count):
        click.echo(f"Hello, {name}")


@click.group()
def cli():
    pass

@cli.command()
def initdb():
    click.echo("Initialized the database")

@cli.command()
def dropdb():
    click.echo("Dropped the database")

cli.add_command(greet2)

if __name__ == '__main__':
    # greet2()
    cli()