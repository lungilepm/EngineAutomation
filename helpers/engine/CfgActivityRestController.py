import os
import logging as logger

import pytest

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility


class CfgActivityRestController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self._caplog = caplog

    def get_engine_rest_activity_loadlistactivitymetadata_helper(self, language=None, agencyId=None, activityCd=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json'}

        # The parameters of get__engine_rest_activity_loadlistactivitymetadata_helper
        parameters = {
            'language': language,
            'agencyId': agencyId,
            'activityCd': activityCd}

        # The request payload of get__engine_rest_activity_loadlistactivitymetadata_helper
        payload = {
        }

        # Default values to be used
        if not language:
            parameters['language'] = INT_HOST[os.environ.get('ENV', 'language')]

        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        if not activityCd:
            parameters['activityCd'] = INT_HOST[os.environ.get('ENV', 'activityCd')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('/ENGINE/rest/activity/loadListActivityMetaData', payload=payload,
                                             headers=headers, params=parameters)
        logger.info(f"/ENGINE/rest/activity/loadListActivityMetaData, Response\n:{response}")
        return response

    def get_engine_rest_activity_findallforagencyid_helper(self, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json'}

        # The parameters of get_engine_rest_activity_findallforagencyid_helper
        parameters = {
            'agencyId': agencyId}

        # The request payload of get_engine_rest_activity_findallforagencyid_helper
        payload = {
        }

        # Default values to be used
        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ENGINE/rest/activity/findAllForAgencyId', payload=payload,
                                             headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response
