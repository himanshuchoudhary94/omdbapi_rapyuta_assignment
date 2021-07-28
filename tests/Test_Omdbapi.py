import requests
from helpers import omdbapi_helper as api

base_url = "http://www.omdbapi.com"
params = {
    's': 'Harry Potter',
    'apikey': 'a9340413'
}

RESPONSE_API = requests.get(url=base_url, params=params)
status_code = RESPONSE_API.status_code
data = RESPONSE_API.json()


class TestApiFunctional:
    """
    This test suite verifies all the functional test cases of an API
    """

    def test_name_in_api(self):
        """ This test case verifies if name is same as query parameter or not """
        api.verify_name(data,  params['s'])

    def test_imdbID_uniqueness(self):
        """ This test case verifies if the ImdbID of search results are unique or not """
        api.verify_imdbID_uniqueness(data)


class TestApiContract:
    """
    This test suite verifies the contract of an API
    """
    def test_api_contract(self):
        """ This test case verifies the contract of the api"""
        api.verify_contract(data, status_code)