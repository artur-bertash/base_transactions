from web3 import Web3

from web3.middleware import geth_poa_middleware
from eth_account.signers.local import LocalAccount
import configseed

Web3 = Web3(Web3.HTTPProvider(endpoint_uri=configseed.base_rpc))

wallet_address = configseed.address  # ваш адрес
checksum_address = Web3.to_checksum_address(wallet_address)
balance = Web3.eth.get_balance(checksum_address)
#print(f"balance of {wallet_address}={balance} Wei")



ether_balance = Web3.from_wei(balance, 'ether')  # Decimal('1')
gwei_balance = Web3.from_wei(balance, 'gwei')  # Decimal('1000000000')
wei_balance = Web3.to_wei(ether_balance, 'ether')  # 1000000000000000000
#print(f"balance of {wallet_address}={ether_balance} Wei")

#print(ether_balance)
