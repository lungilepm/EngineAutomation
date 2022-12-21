import logging as logger
import os

import pytest

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.genericUtilities import generate_username, write_to_text
from utilities.requestsUtility import RequestsUtility


class LookupCodeRestController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self._caplog = caplog

    def get_mlcs_secure_lookupcodes_findallactivebylookupdefinitionid_helper(self, Accept=None, lookupDefinitionId=None,
                                                                             language=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json'}

        # The parameters of get_mlcs_secure_lookupcodes_findallactivebylookupdefinitionid_helper
        parameters = {
            'Accept': Accept,
            'lookupDefinitionId': lookupDefinitionId,
            'language': language,
            'agencyId': agencyId}

        # The request payload of get_mlcs_secure_lookupcodes_findallactivebylookupdefinitionid_helper
        payload = {
        }

        # Default values to be used
        # if not Accept:
        #     parameters['Accept'] = INT_HOST[os.environ.get('ENV', 'Accept')]

        if not lookupDefinitionId:
            parameters['lookupDefinitionId'] = INT_HOST[os.environ.get('ENV', 'lookupDefinitionId')]

        if not language:
            parameters['language'] = INT_HOST[os.environ.get('ENV', 'language')]

        # if not agencyId:
        #     parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(f"Helper function for MLCS/secure/lookupCodes/findAllActiveByLookupDefinitionId payload :{payload}")
        response = self.requests_utility.get('MLCS/secure/lookupCodes/findAllActiveByLookupDefinitionId',
                                             payload=payload, headers=headers, params=parameters)
        logger.info(f"MLCS/secure/lookupCodes/findAllActiveByLookupDefinitionId, Response\n:{response}")
        return response

    def post_iceauth_api_v2_users_json_helper(self, userMetaData=None, uid=None, surname=None, preferredLanguage=None,
                                              organizationalUnit=None, mail=None, initials=None, givenName=None,
                                              commonName=None, cellN=None):
        temp = generate_username()
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"
        logger.debug(f"Authorization {Authorization}")
        # The headers of the request
        headers = {'Authorization': Authorization, 'compress_token': 'true', 'content-type': 'application/json'}

        # The request payload of post_iceauth_api_v2_users_json_helper
        payload = {
            'userMetaData': userMetaData,
            'uid': uid,
            'surname': surname,
            'preferredLanguage': preferredLanguage,
            'organizationalUnit': organizationalUnit,
            'mail': mail,
            'initials': initials,
            'givenName': givenName,
            'commonName': commonName,
            'cellN': cellN}
        parameters = {

        }
        # Default values to be used
        if not userMetaData:
            payload['userMetaData'] = INT_HOST[os.environ.get('ENV', 'userMetaData')]

        if not uid:
            payload['uid'] = temp['name']

        if not surname:
            payload['surname'] = INT_HOST[os.environ.get('ENV', 'surname')]

        if not preferredLanguage:
            payload['preferredLanguage'] = INT_HOST[os.environ.get('ENV', 'preferredLanguage')]

        if not organizationalUnit:
            payload['organizationalUnit'] = INT_HOST[os.environ.get('ENV', 'organizationalUnit')]

        if not mail:
            payload['mail'] = INT_HOST[os.environ.get('ENV', 'mail')]

        if not initials:
            payload['initials'] = INT_HOST[os.environ.get('ENV', 'initials')]

        if not givenName:
            payload['givenName'] = temp['name']

        if not commonName:
            payload['commonName'] = temp['name']

        if not cellN:
            payload['cellN'] = INT_HOST[os.environ.get('ENV', 'cellN')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('iceauth/api/v2/users/json', payload=payload, headers=headers)
        logger.info(f"iceauth/api/v2/users/json, Response\n:{response}")
        return response

    def get_mlcs_secure_calloutservice_gethierarchymap_helper(self):
        pass
