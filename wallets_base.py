from eth_account import Account
from mnemonic import Mnemonic
import configseed

def create_ethereum_wallets(num_wallets):
    # Enable mnemonic features
    Account.enable_unaudited_hdwallet_features()
    
    # Initialize the Mnemonic instance
    mnemo = Mnemonic("english")
    
    wallets = {}
    
    for i in range(num_wallets):
        # Generate a new 12-word mnemonic
        mnemonic_phrase = mnemo.generate(strength=128)  # 128 bits for 12 words
        
        # Generate an account from the mnemonic
        account = Account.from_mnemonic(mnemonic_phrase)
        
        # Wallet_1 is always a cluster
        wallets[f'Wallet_{i + 1}'] = {
            'mnemonic': mnemonic_phrase,
            'address': account.address,
            'private_key': account.key.hex()
        }
    
    return wallets

    
