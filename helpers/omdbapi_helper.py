import pytest
import jsonschema
from contract import apiContract


def verify_name(data, search_movie_name):
    """ This function verifies if the name is search_movie_name or not
    @param data - JSON Response of the API
    """

    if data['Response'] == 'True':
        for movie in data['Search']:
            assert search_movie_name.lower() in movie['Title'].lower(), "Movie not found"
    else:
        pytest.skip("Movie not found for this search")


def verify_imdbID_uniqueness(data):
    """ This function verifies if Can Relist is True or False
    @param data - JSON Response of the API
    """
    if data['Response'] == 'True':
        movie_ids = []
        for movie in data['Search']:
            movie_ids.append(movie['imdbID'])
        assert len(movie_ids) == len(set(movie_ids)), "Duplicate imdbID"
    else:
        pytest.skip("Movie not found for this search")


def verify_contract(data):
    """ This function verifies if contract of the API response is valid or not
    @param data - JSON Response of the API
    @param statusCode - Status Code of the API response
    """
    schema = apiContract.getApi
    if data['Response'] == 'True':
        try:
            myDict = {}
            v = jsonschema.Draft4Validator((schema))
            for error in sorted(v.iter_errors((data)), key=str):
                myDict[str(error.path)] = str(error.message)
                print(myDict)
                assert len(myDict) == 0, "failures in contract"
        except jsonschema.ValidationError as e:
            print(e.message)
    else:
        pytest.skip("Movie not found for this search")