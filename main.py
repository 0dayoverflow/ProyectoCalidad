import requests
import json


url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': '98450951-b678-4ebb-acff-ff8ba0cee184',
}

json = requests.get(url, params=parameters, headers=headers).json()


coins = json['data']

for x in coins:
    print(x['name'], x['quote']['USD']['price'])