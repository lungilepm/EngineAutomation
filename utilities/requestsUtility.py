import json
import logging as logger
import os

import requests

from configs.hosts_config import INT_HOST


class RequestsUtility(object):
    def __init__(self):
        self.rs_json = None
        self.expected_status_code = None
        self.url = None
        self.status_code = None
        self.env = os.environ.get('ENV', 'intzw')
        self.base_url = INT_HOST[self.env]

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            f"Status code error has occurred for post api call to: {self.url}\n" \
            f"Expected status code {self.expected_status_code} but actual {self.status_code}\n" \
            f"Response Json: {self.rs_json}"

    def get(self, endpoint, payload=None, expected_status_code=200, headers=None, params=None):

        if not headers:
            headers = {"Content-Type": "application/json",
                       "Accept": "*/*",
                       'compress_token': 'true'
                       }

        logger.debug(f"get auth token for '{endpoint}' and authorisation {headers['Authorization']}")
        self.url = self.base_url + endpoint

        request = json.dumps(payload)

        rs_api = requests.get(url=self.url, data=request, headers=headers, params=params)
        loot = rs_api.text
        logger.debug(f"Direct response: '{endpoint}'\nrs_api: {rs_api}\nrs_text{loot}")
        self.expected_status_code = expected_status_code
        self.status_code = int(rs_api.status_code)
        self.assert_status_code()
        if not loot:
            self.rs_json = {"statusCode", self.status_code}
        else:
            self.rs_json = rs_api.json()
            logger.debug(f"return payload for post '{endpoint}'\n{self.rs_json}")
        return self.rs_json

    def post(self, endpoint, payload=None, expected_status_code=200, headers=None, params=None):

        if not headers:
            headers = {"Content-Type": "application/json",
                       "Accept": "*/*",
                       'compress_token': 'true'
                       }

        logger.debug(f"get auth token for '{endpoint}'")

        self.url = self.base_url + endpoint

        request = json.dumps(payload)

        rs_api = requests.post(url=self.url, data=request, headers=headers, params=params)
        loot = rs_api.text
        logger.debug(f"Direct response: '{endpoint}'\n{loot}")
        self.expected_status_code = expected_status_code
        self.status_code = int(rs_api.status_code)
        self.assert_status_code()
        if not loot:
            self.rs_json = {"statusCode", self.status_code}
        else:
            self.rs_json = rs_api.json()
            logger.debug(f"return payload for post '{endpoint}'\n{self.rs_json}")
        return self.rs_json

    def delete(self, endpoint, payload=None, expected_status_code=200, headers=None, params=None):

        if not headers:
            headers = {"Content-Type": "application/json",
                       "Accept": "*/*",
                       'compress_token': 'true'
                       }

        logger.debug(f"get auth token for '{endpoint}'")

        self.url = self.base_url + endpoint

        request = json.dumps(payload)

        rs_api = requests.delete(url=self.url, data=request, headers=headers, params=params)
        loot = rs_api.text
        logger.debug(f"Direct response: '{endpoint}'\n{loot}")
        self.expected_status_code = expected_status_code
        self.status_code = int(rs_api.status_code)
        self.assert_status_code()
        if not loot:
            self.rs_json = {"statusCode", self.status_code}
        else:
            self.rs_json = rs_api.json()
            logger.debug(f"return payload for post '{endpoint}'\n{self.rs_json}")
        return self.rs_json
