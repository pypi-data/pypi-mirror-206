import asyncio
import json
import rich_click as click

from rich.console import Console

from ..utils import wait_for_synced_wallet
from .utils import display_rewards, get_offers_with_claimable_rewards

console = Console()


@click.command("list", short_help="List all offers with dexie rewards")
@click.option(
    "-f",
    "--fingerprint",
    required=True,
    help="Set the fingerprint to specify which wallet to use",
    type=int,
)
@click.option(
    "-j",
    "--json",
    "as_json",
    help="Displays offers as JSON",
    is_flag=True,
    default=False,
    show_default=True,
)
@click.pass_context
def list_cmds(ctx: click.Context, fingerprint, as_json):
    asyncio.run(list_cmds_async(fingerprint, as_json))


async def list_cmds_async(fingerprint, as_json):
    await wait_for_synced_wallet(fingerprint)

    offers_rewards = await get_offers_with_claimable_rewards()
    if as_json:
        click.echo(json.dumps(offers_rewards))
    else:
        if len(offers_rewards) == 0:
            console.print("No rewards to claim", style="bold red")
            return
        display_rewards(offers_rewards)
