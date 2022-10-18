import os
import logging as logger
from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.genericUtilities import generate_username, write_to_text
from utilities.requestsUtility import RequestsUtility


class UserControllerTwo(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_iceauth_api_v2_users_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_v2_users_helper
        parameters = {
            'uid': uid}

        # The request payload of get_iceauth_api_v2_users_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'username')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users', payload=payload, headers=headers,
                                             params=parameters)
        return response
