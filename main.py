import balance
import configseed
import wallets_base
import welcome
import os, json

def create_next_cluster(data):
    directory = 'base_transactions/data'
    index = 1
    while True:
        filename = f"data{index}.json"
        filepath = os.path.join(directory, filename)
        if not os.path.exists(filepath):
            with open(filepath, 'w') as f:
                json.dump(data, f)  # Creates an empty JSON file
            print(f"Created file: {filepath}")
            break
        index += 1


data = wallets_base.create_ethereum_wallets(5)

create_next_cluster(data)

print('Please send some eth to the following address - ', data["Wallet_1"]["address"])
