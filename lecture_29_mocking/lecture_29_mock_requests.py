import requests
from requests import Timeout
import unittest
from unittest.mock import Mock

requests = Mock()


def get_data():
    r = requests.get('http://localhost:8080/api/data')
    if r.status_code == 200:
        return r.json()
    return None


def log_request(url):
    print(f"Requesting {url}")

    response = Mock()
    response.status_code = 200
    response.json.return_value = {
        'key': 'value'
    }
    return response


class TestAPI(unittest.TestCase):
    def test_get_data(self):
        requests.get.side_effect = log_request
        data = get_data()
        assert data['key'] == 'value'

    def test_get_data_timeout(self):
        requests.get.side_effect = Timeout
        with self.assertRaises(Timeout):
            get_data()


if __name__ == '__main__':
    unittest.main()
