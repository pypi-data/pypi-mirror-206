import random
import click

@click.command()
@click.option("--name", prompt="your name", help="name of the person to greet")
def say_hello(name):
    click.echo(f"hi, {name}!")

say_hello()
