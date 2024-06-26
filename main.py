import balance
import configseed
import wallets_base
import welcome
import os, json
import balance
import current_price
import time


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


data = wallets_base.create_ethereum_wallets(5)

create_next_cluster(data)
cluster_address = data["Wallet_1"]["address"]
print('Please send some eth to the following address - ', cluster_address)
ser_input = input("Please enter 'Y' if you sent it or 'N' if you didn't: ").strip().lower()

balance = balance.check_balance(cluster_address)
#print(f"balance of {wallet_address}={balance} Wei")
if (balance*int(current_price.get_ethereum_price())) < 1:
    print('The transaction wasnt completed.')
    while True:
        print('The app will automatically check whether you have eth in 15 seconds')
        time.sleep(15)
        if balance * current_price.get_ethereum_price() > 1:
            break
    print('Congrats. You have enough ETH to cover the gas fees.')
print('balance - ', balance)



