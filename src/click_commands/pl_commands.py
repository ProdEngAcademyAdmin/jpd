import click
from src.modules.pipeline import Pipeline


@click.group()
def pl():
    """Commands to make operations on JFrog Pipeline"""


pl.add_command(Pipeline.create_integrations)
pl.add_command(Pipeline.create_pipeline_source)
pl.add_command(Pipeline.trigger_pipeline)

