import click
from click_modules import rt_commands
from click_modules import xray_commands


@click.group()
def jpd():
    pass


jpd.add_command(rt_commands.rt)
jpd.add_command(xray_commands.xray)

if __name__ == '__main__':
    jpd()

