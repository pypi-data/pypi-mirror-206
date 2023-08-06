from rich import box
from rich.console import Console
from rich.table import Table
from rich.text import Text

from chia.types.blockchain_format.sized_bytes import bytes32
from chia.wallet.trading.offer import Offer

from ..config import dexie_api_url, dexie_url
from ..services import wallet_rpc_client as wallet_rpc_client
from ..services.dexie_api import Api, get_dexie_bs58_offer_hash


async def create_claims(offers_rewards):
    claims = []
    for offer_reward in offers_rewards:
        maker_puzzle_hash = bytes32.from_hexstr(offer_reward["maker_puzzle_hash"])
        (
            public_key,
            signature,
            signing_mode,
        ) = await sign_claim(
            offer_reward["id"],
            offer_reward["date_rewards_since"],
            maker_puzzle_hash,
        )

        # return offer hash, signature, pk, and puzzle hash
        claim_info = {
            "offer_id": offer_reward["id"],
            "signature": signature,
            "public_key": public_key,
        }
        claims.append(claim_info)
    return claims


async def get_offers_with_claimable_rewards():
    try:
        offers = await wallet_rpc_client.get_all_offers()

        offer_ids = []
        for offer in offers:
            offer_hash = get_dexie_bs58_offer_hash(Offer.from_bytes(offer.offer))
            offer_ids.append(offer_hash)

        result = await Api(dexie_api_url).get_offers_with_claimable_rewards(offer_ids)
        return result["offers"]
    except Exception as e:
        Console(stderr=True, style="bold red").print(e)
        return []


async def sign_claim(
    offer_id: str, date_rewards_since: str, maker_puzzle_hash: bytes32
):
    message = f"Claim liquidity rewards for {offer_id} since {date_rewards_since}"
    return await wallet_rpc_client.sign_message_by_puzzle_hash(
        maker_puzzle_hash, message
    )


async def claim_rewards(claims_payload):
    result = await Api(dexie_api_url).claim_rewards(claims_payload)
    return result


def display_rewards(offers_rewards):
    table = Table(box=box.ROUNDED)

    table.add_column("Offer", justify="center", no_wrap=True)
    table.add_column("Rewards (DBX)", justify="right", style="bright_cyan")

    for offer_reward in offers_rewards:
        offer_hash = Text(offer_reward["id"])
        offer_hash.stylize("bold dodger_blue2")
        offer_hash.stylize(f"link {dexie_url}/offers/{offer_reward['id']}")
        amount = "{0:0.3f}".format(offer_reward["claimable_rewards"])
        table.add_row(
            offer_hash,
            amount,
        )

    Console().print(table)
