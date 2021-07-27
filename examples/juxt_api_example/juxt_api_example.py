import json

import requests

JUXT_CONFIGURATION = {
  "name": "IEX vs Yahoo Finance - API Example",
  "description": "IEX vs Yahoo Finance - API Example",
  "key_columns": [
    "Ticker"
  ],
  "absolute_tolerance": 0,
  "relative_tolerance": 0,
  "side1_name": "IEX",
  "side2_name": "Yahoo Finance",
  "ignore_extra_columns": False,
  "is_public": False,
  "ignore_columns": [
    "Sector"
  ],
  "columns_config": {
    "Volume": {
      "relative_tolerance": 0.1
    },
    "SharesOutstanding": {
      "relative_tolerance": 0.01
    }
  }
}

ACCESS_TOKEN = '{ENTER_YOUR_ACCESS _TOKEN}'

REQUEST_HEADERS = {
    'authorization': f"Bearer {ACCESS_TOKEN}",
    'accept': 'application/json, text/plain, */*'
}

if __name__ == '__main__':
    # create a juxt session
    response = requests.get(f'https://juxt.io/session/newSession', headers=REQUEST_HEADERS)
    session_id = response.json()['sessionId']

    # update the configuration
    response = requests.post(f'https://juxt.io/session/updateSession?session={session_id}',
                                headers=REQUEST_HEADERS, data=json.dumps(JUXT_CONFIGURATION))

    # upload side 1
    response = requests.post(f'https://juxt.io/session/upload/file?session={session_id}',
                                headers=REQUEST_HEADERS,
                                files={'file': open('/Users/ezrakatz/PycharmProjects/interflowlabs-places-report/example_2/data/iexfinance.csv', 'rb')})

    # upload side 2
    response = requests.post(f'https://juxt.io/session/upload/file?session={session_id}',
                                headers=REQUEST_HEADERS,
                                files={'file': open('/Users/ezrakatz/PycharmProjects/interflowlabs-places-report/example_2/data/yfinance.csv', 'rb')})

    # and, finally, submit
    response = requests.get(f'https://juxt.io/session/submit?session={session_id}', headers=REQUEST_HEADERS)

    # print the comparison summary
    print(response.json()['summary'])
