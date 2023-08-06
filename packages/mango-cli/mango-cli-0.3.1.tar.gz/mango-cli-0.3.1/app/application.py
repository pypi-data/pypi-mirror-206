import pyfiglet
import click
from .handlers.download_data import download_data


pyfiglet.print_figlet("Mangosoft")

@click.group()
@click.version_option()
def cli():
    pass



@cli.command(help="Download data from a table")
def download():
    download_data()
    