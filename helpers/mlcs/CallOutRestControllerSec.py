import os
import logging as logger
from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.genericUtilities import generate_username, write_to_text
from utilities.requestsUtility import RequestsUtility


class CallOutRestControllerSec(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_mlcs_secure_calloutservice_gethierarchymap_helper(self, ):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json'}

        # The parameters of get_mlcs_secure_calloutservice_gethierarchymap_helper
        parameters = {
        }

        # The request payload of get_mlcs_secure_calloutservice_gethierarchymap_helper
        payload = {
        }

        # Default values to be used

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('MLCS/secure/callOutService/getHierarchyMap', payload=payload,
                                             headers=headers, params=parameters)
        return response
