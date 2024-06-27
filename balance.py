from web3 import Web3
import configseed

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(endpoint_uri=configseed.base_rpc))

def check_balance(address):
    # Convert the address to a checksum address
    checksum_address = web3.to_checksum_address(address)
    
    # Get the balance in Wei
    balance_wei = web3.eth.get_balance(checksum_address)
    
    # Return the balance in Wei
    return balance_wei
