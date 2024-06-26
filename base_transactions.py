from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account.signers.local import LocalAccount
from typing import Optional, Dict, Union
import configseed
ab = 'ya ebal v rot'
# не переживаем, что адрес одинаковый
  # checksum
  # checksum

# Create an instance of Web3
w3 = Web3(Web3.HTTPProvider('https://base.llamarpc.com'))

# Inject middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Enable unaudited HD wallet features
w3.eth.account.enable_unaudited_hdwallet_features()

# hex адрес


def build_txn(
    *,
    web3: Web3,
    from_address: str, 
    to_address: str,  
    amount: float,  
) -> Dict[str, Union[int, str]]:

    gas_price = web3.eth.gas_price

    gas = 2_000_000  # ставим побольше


    nonce = web3.eth.get_transaction_count(from_address)

    txn = {
        'chainId': web3.eth.chain_id,
        'from': from_address,
        'to': to_address,
        'value': int(web3.to_wei(amount, 'ether')),
        'nonce': nonce, 
        'gasPrice': gas_price,
        'gas': gas,
    }
    return txn
def send_sign_transaction(my_address, someone_address, amount_of_eth, memo): 
    account = w3.eth.account.from_mnemonic(memo)
    
    private_key = account._private_key  
    transaction = build_txn(
        web3=w3,
        from_address=my_address,
        to_address=someone_address,
        amount=amount_of_eth,
    )


    signed_txn = w3.eth.account.sign_transaction(transaction, private_key)

    txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    return(txn_hash.hex()) 
