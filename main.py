import balance
import configseed
import wallets_base
import welcome
import os, json
import balance
import current_price
import time
import base_transactions

print(base_transactions.ab)
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
print('Please send some eth to the following address - ', cluster_address)
ser_input = input("Please enter 'Y' if you sent it or 'N' if you didn't: ").strip().lower()

balance = balance.check_balance(cluster_address)
#print(f"balance of {wallet_address}={balance} Wei")
if (balance*int(current_price.get_ethereum_price())) < 1:
    print('The transaction wasnt completed.')
    while True:
        print('The app will automatically check whether you have eth in 15 seconds')
        time.sleep(15)
        if balance * current_price.get_ethereum_price() > 40:
            break
    print('Congrats. You have enough ETH to cover the gas fees.')
print('The amount of ETH on the cluster address- ', balance)


#send some eth to the dependent addresses
for i in range(2, len(data)+1):
    for _ in range(5):
        dependent_address = data[f"Wallet_{i}"]['address']
        print('sending some eth to - ', dependent_address)
        base_transactions.send_sign_transaction(cluster_address, dependent_address, 0.00000000000001, cluster_memo)
        time.sleep(5)



