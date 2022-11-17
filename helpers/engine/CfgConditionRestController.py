import logging as logger
import os

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility


class CfgConditionRestController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_engine_rest_condition_findbycomponentid_helper(self, componentGUID=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json'}

        # The parameters of get_engine_rest_condition_findbycomponentid_helper
        parameters = {
            'componentGUID': componentGUID}

        # The request payload of get_engine_rest_condition_findbycomponentid_helper
        payload = {
        }

        # Default values to be used
        if not componentGUID:
            parameters['componentGUID'] = INT_HOST[os.environ.get('ENV', 'componentGUID')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ENGINE/rest/condition/findByComponentId', payload=payload,
                                             headers=headers, params=parameters)
        return response
