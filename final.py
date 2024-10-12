import os
import json
import time
import random
from web3 import Web3
from web3.middleware import geth_poa_middleware
from eth_account import Account
from mnemonic import Mnemonic



welcome_art = r"""
 __        __   _                            _          _   _ 
 \ \      / /__| | ___ ___  _ __ ___   ___  | |_ ___   | | | |
  \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \ | __/ _ \  | | | |
   \ V  V /  __/ | (_| (_) | | | | | |  __/ | || (_) | | |_| |
    \_/\_/ \___|_|\___\___/|_| |_| |_|\___|  \__\___/   \___/ 
                                                             
                                                             
                                                             
                   created by Artur Bertsash                  
"""

welcome_str = 'What Can this script do? - It can spam many transactions in Base network'

print(welcome_art + '\n\n' + welcome_str)


# Initialize Web3
w3 = Web3(Web3.HTTPProvider('https://base.llamarpc.com'))
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

# Enable unaudited HD wallet features
Account.enable_unaudited_hdwallet_features()

def create_ethereum_wallets(num_wallets):
    mnemo = Mnemonic("english")
    wallets = {}
    
    for i in range(num_wallets):
        mnemonic_phrase = mnemo.generate(strength=128)
        account = Account.from_mnemonic(mnemonic_phrase)
        wallets[f"Wallet_{i+1}"] = {
            'mnemonic': mnemonic_phrase,
            'address': account.address,
            'private_key': account.key.hex()
        }
    
    return wallets

def save_wallets(wallets):
    directory = 'base_transactions/data'
    os.makedirs(directory, exist_ok=True)
    filename = "wallets.json"
    filepath = os.path.join(directory, filename)
    with open(filepath, 'w') as f:
        json.dump(wallets, f, indent=2)
    print(f"Wallets saved to: {filepath}")

def load_wallets():
    filepath = os.path.join('base_transactions/data', 'wallets.json')
    with open(filepath, 'r') as f:
        return json.load(f)

def wait_for_transaction(txn_hash, max_attempts=10):
    for attempt in range(max_attempts):
        try:
            tx = w3.eth.get_transaction(txn_hash)
            if tx and tx['blockNumber'] is not None:
                return w3.eth.get_transaction_receipt(txn_hash)
            print(f"Attempt {attempt + 1}/{max_attempts}: Transaction pending...")
        except Exception as e:
            print(f"Attempt {attempt + 1}/{max_attempts}: Error checking transaction status: {e}")
        time.sleep(2)
    print(f"Transaction {txn_hash.hex()} not confirmed after {max_attempts} attempts.")
    return None

def send_transaction(from_wallet, to_address, amount, max_retries=3):
    for retry in range(max_retries):
        try:
            nonce = w3.eth.get_transaction_count(from_wallet['address'])
            gas_price = w3.eth.gas_price
            gas = 2_000_000  

            
            max_amount = w3.eth.get_balance(from_wallet['address']) - (gas * gas_price*2)
            if w3.to_wei(amount, 'ether') > max_amount:
                amount = w3.from_wei(max_amount, 'ether')
                print(f"Adjusting amount to {amount} ETH due to insufficient balance")

            if amount <= 0:
                print("Amount to send is zero or negative. Skipping transaction.")
                return False

            txn = {
                'nonce': nonce,
                'to': to_address,
                'value': w3.to_wei(amount, 'ether'),
                'gas': gas,
                'gasPrice': gas_price,
                'chainId': w3.eth.chain_id,
            }

            signed_txn = w3.eth.account.sign_transaction(txn, from_wallet['private_key'])
            txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)
            print(f"Transaction sent: {txn_hash.hex()}")
            receipt = wait_for_transaction(txn_hash)
            if receipt:
                print(f"Transaction confirmed in block {receipt['blockNumber']}")
                return True
            else:
                print("Transaction not confirmed. It may still be pending.")
                return False
        except Exception as e:
            print(f"Error sending transaction (attempt {retry + 1}/{max_retries}): {e}")
            if retry < max_retries - 1:
                print("Retrying in 5 seconds...")
                time.sleep(5)
            else:
                print("Max retries reached. Moving to the next transaction.")
                return False

def main():
    
    wallets = create_ethereum_wallets(5)
    save_wallets(wallets)

    print("5 Ethereum wallets have been created.")
    print(f"Please send some ETH to this address: {wallets['Wallet_1']['address']}")
    input("Press Enter after you've sent the ETH...")
    number_of_tries = input('Enter number of tries - ')
    
    wallets = load_wallets()

    
    balance = w3.eth.get_balance(wallets['Wallet_1']['address'])
    eth_balance = w3.from_wei(balance, 'ether')
    print(f"Balance of Wallet 1: {eth_balance} ETH")

    if eth_balance == 0:
        print("No funds received. Exiting.")
        return
    print()
    
    for i in range(int(number_of_tries)):  
        print(f"\nTransaction {i+1}")
        from_wallet_num = random.randint(1, 5)
        to_wallet_num = random.randint(1, 5)
        if from_wallet_num == to_wallet_num:
            
            print('The same wallet')
            continue
        from_wallet = wallets[f"Wallet_{from_wallet_num}"]
        to_wallet = wallets[f"Wallet_{to_wallet_num}"]

        from_balance = w3.eth.get_balance(from_wallet['address'])
        if from_balance == 0:
            print(f"Wallet {from_wallet_num} has zero balance. Exiting.")
            continue

        # Calculate the maximum amount that can be sent (balance - gas cost)
        gas_price = w3.eth.gas_price
        max_amount = from_balance - (21000 * gas_price)
        
        if max_amount <= 0:
            print(f"Wallet {from_wallet_num} has insufficient balance for transaction. Exiting.")
            continue
        
        
        print(f"Attempting to send {max_amount} ETH from Wallet {from_wallet_num} to Wallet {to_wallet_num}")
        success = send_transaction(from_wallet, to_wallet['address'], max_amount)
        
        if success:
            print("Waiting 5 seconds before the next transaction...")
            time.sleep(5)
        else:
            print("Waiting 10 seconds before the next transaction...")
            time.sleep(10)

    # Final balance check
    
    final_balance = w3.eth.get_balance(wallets['Wallet_1']['address'])
    final_eth_balance = w3.from_wei(final_balance, 'ether')
    print(f"\nFinal balance of Wallet 1: {final_eth_balance} ETH")

if __name__ == "__main__":
    main()