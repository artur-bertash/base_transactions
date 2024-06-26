import requests

def get_ethereum_price():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    params = {
        'ids': 'ethereum',
        'vs_currencies': 'usd'
    }

    try:
        response = requests.get(url, params=params)
        data_price = response.json()
        ethereum_price = data_price['ethereum']['usd']
        return ethereum_price
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None
    
print(int(get_ethereum_price()))



