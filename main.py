import balance
import configseed
import wallets_base
import welcome
import os, json
import balance
import current_price
import time
import base_transactions
import random 
print(base_transactions.ab)
from web3 import Web3
import configseed

# Initialize Web3
web3 = Web3(Web3.HTTPProvider(endpoint_uri=configseed.base_rpc))

def check_balance(address):
    # Convert the address to a checksum address
    checksum_address = web3.to_checksum_address(address)
    
    # Get the balance in Wei
    balance_wei = web3.eth.get_balance(checksum_address)
    
    # Convert the balance to Ether
    balance_ether = web3.from_wei(balance_wei, 'ether')
    
    return float(balance_ether)

def create_next_cluster(data):
    directory = 'data'
    
    print(directory)
    index = 1
    os.makedirs(directory, exist_ok=True)  # Create directory if it doesn't exist
    while True:
        filename = f"data{index}.json"
        filepath = os.path.join(directory, filename)
        print(filepath)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump(data, f)  
            print(f"Created file: {filepath}")
            break
        index += 1

#create 5 wallets (1 main and 4 dependents)
data = wallets_base.create_ethereum_wallets(5)

create_next_cluster(data)
cluster_address = data["Wallet_1"]["address"]
cluster_memo = data["Wallet_1"]["mnemonic"]
cluster_key = data["Wallet_1"]["private_key"]
print('cluster address - ', cluster_address)
print('Please send some eth to the following address - ', cluster_address)
ser_input = input("Please enter 'Y' if you sent it or 'N' if you didn't: ").strip().lower()

balance = check_balance(cluster_address)
print('balance is - ', balance)
#print(f"balance of {wallet_address}={balance} Wei")
""" if (balance*int(current_price.get_ethereum_price())) < 1:
    print('The transaction wasnt completed.')
    while True:
        print('The app will automatically check whether you have eth in 15 seconds')
        time.sleep(15)
        if balance * current_price.get_ethereum_price() > 40:
            break
    print('Congrats. You have enough ETH to cover the gas fees.')
print('The amount of ETH on the cluster address- ', balance)
 """

def transfer_funds_sequally(wallets):
    