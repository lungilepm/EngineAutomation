import logging as logger
import os

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility

logger.getLogger('faker').setLevel(logger.ERROR)


class UserController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_iceauth_api_users_getusersforagency_helper(self, unallocated=None, includeChildren=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_users_getusersforagency_0_helper
        parameters = {
            'unallocated': unallocated,
            'includeChildren': includeChildren}

        # The request payload of get_iceauth_api_users_getusersforagency_0_helper
        payload = {
        }

        # Default values to be used
        if not unallocated:
            parameters['unallocated'] = INT_HOST[os.environ.get('ENV', 'unallocated')]

        if not includeChildren:
            parameters['includeChildren'] = INT_HOST[os.environ.get('ENV', 'includeChildren')]

        if not agencyId:
            agencyId = INT_HOST[os.environ.get('ENV', 'organizationalUnit')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get(f'ICEAUTH/api/users/getUsersForAgency/{agencyId}', payload=payload,
                                             headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json/{agencyId}, Response {response}")
        return response
