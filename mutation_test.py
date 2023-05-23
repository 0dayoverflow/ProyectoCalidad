import unittest
import main

class TestCoinsMainCrypt(unittest.TestCase):
   
    def test_get_crypto_coins(self):
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

        for params, headers in params:
            with self.subTest(url, params=params, headers=headers):
                obtained = main(params)
                self.assertEqual(obtained, headers,
                                 "triple(%s) should be %s" % (params, headers))
                
if __name__ == "__main__":
    unittest.main()                  