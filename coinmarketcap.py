from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import os
if os.path.exists("env.py"):
    import env


crypto_List = []
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {
  'start': '1',
  'limit': '5',
  'convert': 'USD'
}
headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': os.environ.get("API-key"),
}

session = Session()
session.headers.update(headers)

try:
    response = session.get(url, params=parameters)
    data = json.loads(response.text)
    coins = data['data']

except (ConnectionError, Timeout, TooManyRedirects) as e:
    print(e)


def get_crypto_list():
    for d in data['data']:
        crypto_name_from_api = d['symbol']
        crypto_List.append(crypto_name_from_api)


price_list = []


def get_price_list():
    for x in coins:
        for x['symbol'] in coins:
            price = float((x['quote']['USD']['price']))
        price_list.append(price)
        
# get_price_list()
# print(price_list)
# get_crypto_list()
# print(crypto_List)


# - validate to see if user entered crypto which is in crypto list

# - get crpto price


# def get_crypto_price(crypto_name):
#     price = 0
#     for x in coins:
#         if x['symbol'] == crypto_name:
#             price = float((x['quote']['USD']['price']))
#     print(price)
        

# def display_all_crypto_prices():
    

# def get_all_prices():
#     for x in coins:
#         for x['symbol'] in coins:
#             price = float((x['quote']['USD']['price']))
#         print(price)


def get_all_cryptos():
    for x in crypto_List:
        print(x)
   



get_crypto_list()
get_price_list()

for f, b in zip(crypto_List, price_list):
    print(f, b)


# get_all_cryptos()


# get_all_cryptos()
# get_all_prices()

# get_crypto_price('ETH')