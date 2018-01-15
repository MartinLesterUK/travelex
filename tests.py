import unittest
import requests
import json
from pprint import pprint

class SimpleTestCase(unittest.TestCase):

    def testSource(self):
        url = "http://localhost:8080/api/v1/countries/source"
        print "\nExpecting OK: " + url

        headers = {'Accept' : 'application/json'}
        resp = requests.get(url, headers=headers)

        assert resp.status_code == 200
        assert resp.json()[0].get("name") == "Australia"
    

    def testDest(self):
        url = "http://localhost:8080/api/v1/countries/destination"
        print "\nExpecting OK: " + url

        headers = {'Accept' : 'application/json'}
        resp = requests.get(url, headers=headers)

        assert resp.status_code == 200
        assert resp.json()[0].get("isoCode") == "FR"


    def testError(self):
        url = "http://localhost:8080/api/v1/countries"
        print "\nExpecting FAIL: " + url
        resp = requests.get(url)
        assert resp.status_code == 404


if __name__ == "__main__":
    unittest.main() # run all tests
                        
