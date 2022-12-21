import os

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility
import logging as logger


class CfgEntityAttributeRestController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_engine_rest_cfgentityattribute_findbyentitytypecd_helper(self, entityTypeCd=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json'}

        # The parameters of get_engine_rest_cfgentityattribute_findbyentitytypecd_helper
        parameters = {
            'entityTypeCd': entityTypeCd,
            'agencyId': agencyId}

        # The request payload of get_engine_rest_cfgentityattribute_findbyentitytypecd_helper
        payload = {
        }

        # Default values to be used
        if not entityTypeCd:
            parameters['entityTypeCd'] = INT_HOST[os.environ.get('ENV', 'entityTypeCd')]

        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ENGINE/rest/cfgentityattribute/findByEntityTypeCd', payload=payload,
                                             headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response
