import requests 

# get average price 
# use average price to find the difference between that price and the current price 
# use volume, orderbook and historical data to decide the direction of the trend#

base_url = 'https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=USD&days=365&interval=daily' #'https://api.coingecko.com/api/v3/ping'
res = requests.get(base_url)
print(res.json())