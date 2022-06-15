from requests import Request, Session
import json
import pprint
import os
if os.path.exists("env.py"):
    import env 

url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
# url which the api retreives the latest quotes


parameters = {
    'slug': 'bitcoin',
    'convert': 'USD'

}

headers = {
    'X-CMC_PRO_API_KEY': os.environ.get("API"),
    'Accepts': 'application/json'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
