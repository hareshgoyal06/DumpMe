
import requests

def get_crypto_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        return data[symbol]['usd']
    else:
        raise Exception("Error fetching data from CoinGecko API")
