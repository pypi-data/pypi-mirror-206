import rich_click as click

from dexie_rewards import __version__
from .rewards.main import rewards_cmd


@click.group("dexie")
@click.version_option(__version__)
@click.pass_context
def dexie_cmd(ctx: click.Context) -> None:
    pass


dexie_cmd.add_command(rewards_cmd)
