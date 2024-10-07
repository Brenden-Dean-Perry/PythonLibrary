import requests
import pandas as pd

class AlphaVantageAPI:
    _api_key = 'demo'

    def __int__(self, api_key):
        _api_key = api_key

    def get_stock_data(self, ticker: str):
        # API_URL = "https://www.alphavantage.co/query"
        # data = {"function": "TIME_SERIES_DAILY",
             # "symbol": ticker,
             # "outputsize" : "full",
             ## "datatype": "json",
             # "apikey": self._api_key}

        API_URL = 'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey=demo'
        # response = requests.get(API_URL, data)
        response = requests.get(API_URL)
        response_json = response.json()
        print(response_json)
        data = pd.DataFrame.from_dict(response_json['Time Series (Daily)'], orient='index').sort_index(axis=1)
        data = data.rename(columns={'1. open': 'Open', '2. high': 'High', '3. low': 'Low', '4. close': 'Close', '5. volume': 'Volume'})
        data = data[['Open', 'High', 'Low', 'Close', 'Volume']]
        data.tail()  # check OK or not
        return data
