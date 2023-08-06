import pyfiglet
import click
from .handlers.download_data import download_data
import os
import pathlib

version_file = pathlib.Path("VERSION").absolute()
with open(version_file, "r") as fh:
    version = fh.read()

pyfiglet.print_figlet("Mangosoft CLI")

@click.group()
@click.version_option(version)
@click.pass_context
def cli(ctx):
    pass



@cli.command(help="Download data from a table")
def download():
    download_data()
