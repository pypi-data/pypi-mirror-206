from chia.rpc.wallet_rpc_client import WalletRpcClient
from chia.util.bech32m import encode_puzzle_hash


from ..config import (
    address_prefix,
    chia_config,
    chia_root,
    self_hostname,
    wallet_rpc_port,
)
from ..decorators.with_wallet_rpc_client import with_wallet_rpc_client


@with_wallet_rpc_client(self_hostname, wallet_rpc_port, chia_root, chia_config)
async def log_in(wallet_rpc_client: WalletRpcClient, fingerprint):
    return await wallet_rpc_client.log_in(fingerprint)


@with_wallet_rpc_client(self_hostname, wallet_rpc_port, chia_root, chia_config)
async def get_synced(wallet_rpc_client: WalletRpcClient):
    return await wallet_rpc_client.get_synced()


@with_wallet_rpc_client(self_hostname, wallet_rpc_port, chia_root, chia_config)
async def get_all_offers(wallet_rpc_client: WalletRpcClient):
    return await wallet_rpc_client.get_all_offers(file_contents=True)


@with_wallet_rpc_client(self_hostname, wallet_rpc_port, chia_root, chia_config)
async def sign_message_by_puzzle_hash(
    wallet_rpc_client: WalletRpcClient, puzzle_hash, message
):
    address = encode_puzzle_hash(puzzle_hash, address_prefix)
    return await wallet_rpc_client.sign_message_by_address(address, message)
