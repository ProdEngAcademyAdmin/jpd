import click
from src.modules.xray import Xray


@click.group()
def xray():
    """Commands to make operations on Xray"""


xray.add_command(Xray.create_watch)
xray.add_command(Xray.create_policy)

