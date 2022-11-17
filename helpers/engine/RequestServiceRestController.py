import logging as logger
import os

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility


class RequestServiceRestController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_engine_rest_requestservice_helper(self, lookupDefinitionId=None, language=None, gatAgencyId=None,
                                              agencyId=None, serviceCode=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json;charset=UTF-8',
            'Content-Type': 'application/json'}

        # The parameters of get_engine_rest_requestservice_helper
        parameters = {
            'lookupDefinitionId': lookupDefinitionId,
            'language': language,
            'gatAgencyId': gatAgencyId,
            'agencyId': agencyId,
            'serviceCode': serviceCode}

        # The request payload of get_engine_rest_requestservice_helper
        payload = {
        }

        # Default values to be used
        if not lookupDefinitionId:
            parameters['lookupDefinitionId'] = INT_HOST[os.environ.get('ENV', 'lookupDefinitionId')]

        if not language:
            parameters['language'] = INT_HOST[os.environ.get('ENV', 'language')]

        if not gatAgencyId:
            parameters['gatAgencyId'] = INT_HOST[os.environ.get('ENV', 'gatAgencyId')]

        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        if not serviceCode:
            parameters['serviceCode'] = INT_HOST[os.environ.get('ENV', 'serviceCode')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ENGINE/rest/requestservice', payload=payload, headers=headers,
                                             params=parameters)
        return response
