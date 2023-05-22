import unittest
import requests

#Prueba de InerOperabilidad
class InteroperabilityTest(unittest.TestCase):
    def test_api_call(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '5',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '98450951-b678-4ebb-acff-ff8ba0cee184',
        }

        response = requests.get(url, params=parameters, headers=headers)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('data' in response.json())

    def test_print_coins(self):
        url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
        parameters = {
            'start': '1',
            'limit': '5',
            'convert': 'USD'
        }
        headers = {
            'Accepts': 'application/json',
            'X-CMC_PRO_API_KEY': '98450951-b678-4ebb-acff-ff8ba0cee184',
        }

        response = requests.get(url, params=parameters, headers=headers)
        coins = response.json()['data']

        for coin in coins:
            self.assertTrue('name' in coin)
            self.assertTrue('quote' in coin)
            self.assertTrue('USD' in coin['quote'])
            self.assertTrue('price' in coin['quote']['USD'])

    # Add more test cases if needed

if __name__ == '__main__':
    unittest.main()
