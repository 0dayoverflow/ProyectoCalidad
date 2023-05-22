import unittest
import requests

class TestCoinMarketCapAPI(unittest.TestCase):
    def test_get_top_five_cryptocurrencies(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        params = {
            'start':'1',
            'limit':'5',
            'convert':'USD'
        }
        headers = {
            'Accept': 'application/json',
            'X-CMC_PRO_API_KEY': '98450951-b678-4ebb-acff-ff8ba0cee184',
        }
        response = requests.get(url, params=params, headers=headers)
        json_data = response.json()

        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(json_data)

        cryptocurrencies = json_data['data']
        self.assertEqual(len(cryptocurrencies), 5)

        for currency in cryptocurrencies:
            self.assertIsNotNone(currency['name'])
            self.assertIsNotNone(currency['quote']['USD']['price'])
            print(currency['name'], currency['quote']['USD']['price'])

if __name__ == '__main__':
    unittest.main()
