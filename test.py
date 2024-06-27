import base_transactions
import balance
import time
wallets = {
    "Wallet_1": {
        "mnemonic": "kit green loud wrap present brave pluck barely anger solar exercise yard",
        "address": "0xF250770c1f1fC303F56e34267460965EEb78E7cB",
        "private_key": "0xc574c0c8ff7ff25b1fbbb136219609d3bd504f89b01730b105a426f7712dd80a"
    },
    "Wallet_2": {
        "mnemonic": "myth pear athlete miracle enable inform jeans custom occur foot decide apart",
        "address": "0x2105B84cAd8fB20E27156AEE292e4252bb03b322",
        "private_key": "0xab73d895e414e79329c9724d96363c3ea2d77f36ae79fe44bca6ec9b39596b05"
    },
    "Wallet_3": {
        "mnemonic": "photo fog kangaroo awful card elephant enemy say couch vocal horn eyebrow",
        "address": "0xA827B42E077Ad516D1D9826B75df6Da210bD90e1",
        "private_key": "0x995441a81429939d51c523da2451b95bca66b999d0db4c441e8797cf80d6f635"
    },
    "Wallet_4": {
        "mnemonic": "head turtle glad possible inform under air skate gaze grid pencil annual",
        "address": "0xE835e1358A19dA658bB3EF376946151A2A6D82A9",
        "private_key": "0x3282267cd2890f4aff2f1055bcb3d5a7a57d722d2ab29b193e42abe8b651efa0"
    },
    "Wallet_5": {
        "mnemonic": "umbrella human among demand civil column chicken horn bright rely evidence amount",
        "address": "0xEa83B249ed636f6769AD2a5A1761B6c9218d1E09",
        "private_key": "0xd5443dd2a1a28d2209326c1debaa997145b4dc659d35e7ebf129d4c582db4d64"
    }
}


def transfer_funds_sequally(wallets):
    wallet_keys = list(wallets.keys())
    first_wallet = wallets[wallet_keys[0]]
    gas_limit = 21000  # Standard gas limit for a simple ETH transfer
    gas_price = 20 * 10**9  # 20 Gwei in wei
    
    cluster_address = wallets['Wallet_1']['address']
    cluster_memo = wallets['Wallet_1']['mnemonic']
    balance_cluster = balance.check_balance(cluster_address) 
    
    print('Balance of the cluster account:', balance_cluster)
    print('Wallet keys:', wallet_keys)
    print('Gas price:', gas_price)
    
    # Calculate the amount to send, ensuring it's a positive integer
    
    
    
    # Example of sending transaction
    for n in range(2, 6): #send enough eth to cover fees 
        dependent_address = wallets[f'Wallet_{n}']['address']
        amount_to_send =    150000000000000 #0.00015 ether
        base_transactions.send_sign_transaction(cluster_address, dependent_address, amount_to_send, cluster_memo)
        print('Gas eth was sent to the wallet number - ', n )
        time.sleep(5)
    
    
    # Example loop for sending to dependent wallets
    for n in range(2, 6):
        dependent_address = wallets[f'Wallet_{n}']['address']
        dependent_memo = wallets[f'Wallet_{n}']['mnemonic']
        amount_to_send =    5900000000000000 #0.0059 ether
        base_transactions.send_sign_transaction(cluster_address, dependent_address, amount_to_send, cluster_memo)
        print('Eth was sent to the wallet number - ', n )
        time.sleep(5)
        base_transactions.send_sign_transaction(dependent_address, cluster_address, amount_to_send, dependent_memo)
        print('Eth was sent back to the cluster address ')
        time.sleep(5)

        
        
   
    
# Call the function
transfer_funds_sequally(wallets)
