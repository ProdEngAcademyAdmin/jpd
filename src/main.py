import click
from src.click_commands import xray_commands, rt_commands, pl_commands


@click.group()
def cli():
    pass


cli.add_command(rt_commands.rt)
cli.add_command(xray_commands.xray)
cli.add_command(pl_commands.pl)

if __name__ == '__main__':
    cli()

