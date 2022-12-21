from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility
import logging as logger


class CfgActivityEditRestController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_engine_rest_activityedit_helper(self, ):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json'}

        # The parameters of get_engine_rest_activityedit_helper
        parameters = {
        }

        # The request payload of get_engine_rest_activityedit_helper
        payload = {
        }

        # Default values to be used

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ENGINE/rest/activityEdit', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response
