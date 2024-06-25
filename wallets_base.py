from eth_account import Account
from mnemonic import Mnemonic

def create_ethereum_wallets(num_wallets):
    # Enable mnemonic features
    Account.enable_unaudited_hdwallet_features()
    
    # Initialize the Mnemonic instance
    mnemo = Mnemonic("english")
    
    wallets = []
    
    for _ in range(num_wallets):
        # Generate a new 12-word mnemonic
        mnemonic_phrase = mnemo.generate(strength=128)  # 128 bits for 12 words
        
        # Generate an account from the mnemonic
        account = Account.from_mnemonic(mnemonic_phrase)
        
        # Store the mnemonic and the account details
        wallets.append({
            'mnemonic': mnemonic_phrase,
            'address': account.address,
            'private_key': account.key.hex()
        })
    
    return wallets

if __name__ == "__main__":
    num_wallets_to_create = 5  # Number of wallets you want to create
    wallets = create_ethereum_wallets(num_wallets_to_create)
    
    for i, wallet in enumerate(wallets):
        print(f"Wallet {i + 1}:")
        print(f"Address: {wallet['address']}")
        print(f"Mnemonic: {wallet['mnemonic']}")
        print(f"Private Key: {wallet['private_key']}")
        print()
