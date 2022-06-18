from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import pprint
import os
if os.path.exists("env.py"):
    import env


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

