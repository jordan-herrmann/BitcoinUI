from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

def cryptoPull():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    parameters = {
        'start':'1',
        'limit':'1',
        'convert':'USD'
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': 'c9c38915-ecfc-4b7c-bec8-7da188301f64'
    }

    session = Session()
    session.headers.update(headers)

    try: 
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        f= open("crypto.json","w", encoding='utf-8')
        f.write(json.dumps(data,ensure_ascii=True))
        f.close()
    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)
