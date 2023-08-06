import rich_click as click

from .list import list_cmds
from .claim import claim_cmds


@click.group("rewards", short_help="Manage your dexie rewards for offers")
@click.pass_context
def rewards_cmd(ctx: click.Context) -> None:
    pass


rewards_cmd.add_command(list_cmds)
rewards_cmd.add_command(claim_cmds)
