import click
from modules.artifactory import Artifactory


@click.group()
def rt():
    """Commands to make operations on JFrog Artifactory"""


rt.add_command(Artifactory.ping)
rt.add_command(Artifactory.storage_info)
rt.add_command(Artifactory.create_repo)

