import requests
import os
import json

from configs.hosts_config import INT_HOST
import logging as logger

class RequestsUtility(object):
    def __init__(self):
        self.status_code = None
        self.env = os.environ.get('ENV', 'intzw')
        self.base_url = INT_HOST[self.env]

    def assert_status_code(self):
        assert self.status_code == self.expected_status_code, \
            f"Status code error has occurred for post api call to: {self.url}" \
            f"Expected status code {self.expected_status_code} but actual {self.status_code}\n" \
            f"Response Json: {self.rs_json}"

    def get(self, endpoint, payload=None, expected_status_code=200, auth=None):

        if not auth:
            headers = {"Content-Type": "application/json",
                       "Accept": "*/*",
                       'compress_token': 'true'
                       }
        else:
            auth
            headers = {
                'Authorization': 'Bearer {}'.format(auth),
                'Content-Type': 'application/json',
                'compress_token': 'true'

            }
            logger.debug(f"get auth token for '{endpoint}' and authorisation {auth}")
        self.url = self.base_url + endpoint

        request = json.dumps(payload)

        rs_api = requests.get(url=self.url, data=request, headers=headers)
        # import pdb
        # pdb.set_trace()
        self.expected_status_code = expected_status_code
        self.status_code = int(rs_api.status_code)
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"return payload for get '{endpoint}'\n{self.rs_json}")
        return self.rs_json

    def post(self, endpoint, payload=None, expected_status_code=200, auth=None):

        if not auth:
            headers = {"Content-Type": "application/json",
                       "Accept": "*/*",
                       'compress_token': 'true'
                       }
        else:
            auth
            headers = {
                'Authorization': 'Bearer {}'.format(auth),
                'Content-Type': 'application/json',
                'compress_token': 'true'

            }
            logger.debug(f"get auth token for '{endpoint}' and authorisation {auth}")

        self.url = self.base_url + endpoint

        request = json.dumps(payload)

        rs_api = requests.post(url=self.url, data=request, headers=headers)
        # import pdb
        # pdb.set_trace()
        self.expected_status_code = expected_status_code
        self.status_code = int(rs_api.status_code)
        self.rs_json = rs_api.json()
        self.assert_status_code()
        logger.debug(f"return payload for post '{endpoint}'\n{self.rs_json}")
        return self.rs_json
