import logging as logger
import os

from configs.hosts_config import INT_HOST
from utilities.requestsUtility import RequestsUtility


class TokenController(object):
    def __init__(self):
        self.requests_utility = RequestsUtility()

    def post_iceauth_oauth_token_params_helper(self, password=None, username=None, client_secret=None, client_id=None,
                                               grant_type=None, realm=None):
        headers = {
            'compress_token': 'true',
            'realm': realm,
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36'}

        # The parameters of post_iceauth_oauth_token_helper
        parameters = {
            'password': password,
            'username': username,
            'client_secret': client_secret,
            'client_id': client_id,
            'grant_type': grant_type
        }
        payload = {

        }
        # Default values to be used
        if not password:
            parameters['password'] = INT_HOST[os.environ.get('ENV', 'password')]

        if not username:
            parameters['username'] = INT_HOST[os.environ.get('ENV', 'username')]

        if not client_secret:
            parameters['client_secret'] = INT_HOST[os.environ.get('ENV', 'client_secret')]

        if not client_id:
            parameters['client_id'] = INT_HOST[os.environ.get('ENV', 'client_id')]

        if not grant_type:
            parameters['grant_type'] = INT_HOST[os.environ.get('ENV', 'grant_type')]
        if not realm:
            headers['realm'] = INT_HOST[os.environ.get('ENV', 'realm')]

        logger.info(f"Helper function for iceauth/api/v2/users/json Authentication: \npayload :{payload}\nparams :{parameters}\nheaders :{headers}")

        response = self.requests_utility.post('ICEAUTH/oauth/token', headers=headers,
                                              params=parameters, payload=payload)
        return response

    def post_iceauth_oauth_token_helper(self, uSub=None, otp=None, refresh_token=None, password=None,
                                        username=None, grant_type=None, client_secret=None, client_id=None, realm=None):

        # The headers of the request
        headers = {
            'compress_token': 'true',
            'realm': realm,
            'Accept': '*/*',
            'Content-Type': 'application/json',
            'User-Agent': 'PostmanRuntime/7.29.2'
        }

        # The parameters of post_iceauth_oauth_token_helper
        parameters = {
        }

        # The request payload of post_iceauth_oauth_token_helper
        payload = {
            'uSub': uSub,
            'otp': otp,
            'refresh_token': refresh_token,
            'password': password,
            'username': username,
            'grant_type': grant_type,
            'client_secret': client_secret,
            'client_id': client_id
        }

        # Default values to be used
        # if not uSub:
        #     payload['uSub'] = INT_HOST[os.environ.get('ENV', 'uSub')]

        # if not otp:
        #     payload['otp'] = INT_HOST[os.environ.get('ENV', 'otp')]

        if not refresh_token:
            payload['refresh_token'] = INT_HOST[os.environ.get('ENV', 'refresh_token')]

        if not password:
            payload['password'] = INT_HOST[os.environ.get('ENV', 'password')]

        if not username:
            payload['username'] = INT_HOST[os.environ.get('ENV', 'username')]

        if not grant_type:
            payload['grant_type'] = INT_HOST[os.environ.get('ENV', 'grant_type')]

        if not client_secret:
            payload['client_secret'] = INT_HOST[os.environ.get('ENV', 'client_secret')]

        if not client_id:
            payload['client_id'] = INT_HOST[os.environ.get('ENV', 'client_id')]
        if not realm:
            headers['realm'] = INT_HOST[os.environ.get('ENV', 'realm')]

        logger.info(f"Helper function for ICEAUTH/oauth/token payload :{payload} \nheaders: {headers}\nparams: {parameters}")
        response = self.requests_utility.post('ICEAUTH/oauth/token', payload=payload, headers=headers,
                                              params=parameters)
        return response
