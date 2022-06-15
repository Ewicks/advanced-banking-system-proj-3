from requests import Request, Session
import json
import pprint
url = 'https://pro-api.coinmarketcap.com/v2/cryptocurrency/quotes/latest'
# url which the api retreives the latest quotes 


parameters = {
    'slug': 'bitcoin',
    'convert': 'USD'

}

headers = {
    'Accepts': 'application/json',
    'X-CMC_PRO_API_KEY': '01a25dc6-2ab9-4b40-9d83-a3af12ce8239'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
