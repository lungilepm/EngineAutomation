import logging as logger

import os

import pytest

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility

logger.getLogger('faker').setLevel(logger.ERROR)


class RolesController(object):
    @pytest.fixture(autouse=True)
    def inject_fixtures(self, caplog):
        self._caplog = caplog

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def post_iceauth_api_roles_addusertorole_helper(self, uid=None, roleName=None, clearCache=True, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization}

        # The parameters of post_iceauth_api_roles_addusertorole_helper
        parameters = {
            'uid': uid,
            'roleName': roleName,
            'clearCache': True,
            'agencyId': agencyId}

        # The request payload of post_iceauth_api_roles_addusertorole_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'username')]

        if not roleName:
            parameters['roleName'] = INT_HOST[os.environ.get('ENV', 'roleName')]

        if not clearCache:
            parameters['clearCache'] = INT_HOST[os.environ.get('ENV', 'clearCache')]

        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(f"Helper function for ICEAUTH/api/roles/addUserToRole payload :{payload}")
        response = self.requests_utility.post('ICEAUTH/api/roles/addUserToRole', payload=payload, headers=headers,
                                              params=parameters, expected_status_code=201)
        logger.info(f"Response function for ICEAUTH/api/roles/addUserToRole payload :{response}")
        return response

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
        logger.info(
            f"ICEAUTH/api/v2/users, Response\n:{response}")
        return response

    def post_iceauth_api_roles_json_addusertorole_helper(self, uid=None, agencyId=None, roleName=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_roles_json_addusertorole_helper
        parameters = {
        }

        # The request payload of post_iceauth_api_roles_json_addusertorole_helper
        payload = {
            'uid': uid,
            'agencyId': agencyId,
            'roleName': roleName}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        if not agencyId:
            payload['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        if not roleName:
            payload['roleName'] = INT_HOST[os.environ.get('ENV', 'roleName')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/roles/json/addUserToRole', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/roles/json/addUserToRole, Response\n:{response}")
        return response

    def delete_iceauth_api_roles_removeuserfromrole_helper(self, uid=None, roleName=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization}

        # The parameters of delete_iceauth_api_roles_removeuserfromrole_helper
        parameters = {
            'uid': uid,
            'roleName': roleName,
            'agencyId': agencyId}

        # The request payload of delete_iceauth_api_roles_removeuserfromrole_helper
        payload = {
        }

        # Default values to be used
        # if not uid:
        #     parameters['uid'] = INT_HOST[os.environ.get('ENV', 'u')]
        #
        # if not roleName:
        #     parameters['roleName'] = INT_HOST[os.environ.get('ENV', 'roleName')]
        #
        # if not agencyId:
        #     parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.delete('ICEAUTH/api/roles/removeUserFromRole', payload=payload,
                                                headers=headers, params=parameters, expected_status_code=201)
        logger.info(f"ICEAUTH/api/roles/removeUserFromRole, Response\n:{response}")
        return response

    def delete_iceauth_api_roles_json_removeuserfromrole_helper(self, uid=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of delete_iceauth_api_roles_json_removeuserfromrole_helper
        parameters = {
        }

        # The request payload of delete_iceauth_api_roles_json_removeuserfromrole_helper
        payload = [{'roleName': 'AuthAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'SysAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'AudAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'CfgImporter',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'CFGADMIN',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'LookupAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'CFGTEMPLATE',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'AppAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'AuthUser',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'System',
                    'agencyId': agencyId,
                    'uid': uid}]

        # # Default values to be used
        # if not uid:
        #     payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]
        #
        # if not agencyId:
        #     payload['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]
        #
        # if not roleName:
        #     payload['roleName'] = INT_HOST[os.environ.get('ENV', 'roleName')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.delete('ICEAUTH/api/roles/json/removeUserFromRole', payload=payload,
                                                headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/roles/json/removeUserFromRole, Response\n:{response}")
        return response

    def post__iceauth_api_roles_json_addusertoroles_helper(self, uid=None, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of post__iceauth_api_roles_json_addusertoroles_helper
        parameters = {
        }

        # The request payload of post__iceauth_api_roles_json_addusertoroles_helper
        payload = [{'roleName': 'AuthAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'SysAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'AudAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'CfgImporter',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'CFGADMIN',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'LookupAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'CFGTEMPLATE',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'AppAdmin',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'AuthUser',
                    'agencyId': agencyId,
                    'uid': uid},
                   {'roleName': 'System',
                    'agencyId': agencyId,
                    'uid': uid}]

        # Default values to be used
        # if not uid:
        #     payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]
        #
        # if not agencyId:
        #     payload['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]
        #
        # if not roleName:
        #     payload['roleName'] = INT_HOST[os.environ.get('ENV', 'roleName')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('/ICEAUTH/api/roles/json/addUserToRoles', payload=payload,
                                              headers=headers, params=parameters)
        logger.info(f"/ICEAUTH/api/roles/json/addUserToRoles, Response\n:{response}")

        return response

    def get_iceauth_api_roles_getallroles_helper(self, agencyId=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_roles_getallroles_helper
        parameters = {
            'agencyId': agencyId}

        # The request payload of get_iceauth_api_roles_getallroles_helper
        payload = {
        }

        # Default values to be used
        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/roles/getAllRoles', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response
