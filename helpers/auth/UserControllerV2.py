import logging as logger
import os

from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from utilities.genericUtilities import generate_username
from utilities.requestsUtility import RequestsUtility

logger.getLogger('faker').setLevel(logger.ERROR)


class UserControllerV2(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def get_iceauth_api_v2_users_helper(self, uid=None, expected_code=200):
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
                                             params=parameters, expected_status_code=expected_code)
        logger.info(f"ICEAUTH/api/v2/users, Response\n:{response}")
        return response

    def post_iceauth_api_v2_users_json_helper(self, userMetaData=None, uid=None, surname=None, preferredLanguage=None,
                                              organizationalUnit=None, mail=None, initials=None, givenName=None,
                                              commonName=None, cellN=None):
        person = generate_username()
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': Authorization}

        # The parameters of post_iceauth_api_v2_users_json_helper
        parameters = {
        }

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

        # Default values to be used
        if not userMetaData:
            payload['userMetaData'] = INT_HOST[os.environ.get('ENV', 'userMetaData')]

        if not uid:
            payload['uid'] = person['name']

        if not surname:
            payload['surname'] = person['surname']

        if not preferredLanguage:
            payload['preferredLanguage'] = INT_HOST[os.environ.get('ENV', 'language')]

        if not organizationalUnit:
            payload['organizationalUnit'] = INT_HOST[os.environ.get('ENV', 'organizationalUnit')]

        if not mail:
            payload['mail'] = person['email']

        if not initials:
            payload['initials'] = INT_HOST[os.environ.get('ENV', 'initials')]

        if not givenName:
            payload['givenName'] = person['surname']

        if not commonName:
            payload['commonName'] = person['surname']

        if not cellN:
            payload['cellN'] = INT_HOST[os.environ.get('ENV', 'cellN')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/json', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response\n:{response}")
        return response

    def get_iceauth_api_v2_users_json_getusersforagency_helper(self, unallocated=None, includeChildren=None, force=None,
                                                               agencyId=None, addRoles=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_v2_users_json_getusersforagency_helper
        parameters = {
            'unallocated': unallocated,
            'includeChildren': includeChildren,
            'force': force,
            'agencyId': agencyId,
            'addRoles': addRoles}

        # The request payload of get_iceauth_api_v2_users_json_getusersforagency_helper
        payload = {
        }

        # Default values to be used
        if not unallocated:
            parameters['unallocated'] = INT_HOST[os.environ.get('ENV', 'unallocated')]

        if not includeChildren:
            parameters['includeChildren'] = INT_HOST[os.environ.get('ENV', 'includeChildren')]

        if not force:
            parameters['force'] = INT_HOST[os.environ.get('ENV', 'force')]

        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'organizationalUnit')]

        if not addRoles:
            parameters['addRoles'] = INT_HOST[os.environ.get('ENV', 'addRoles')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/json/getUsersForAgency', payload=payload,
                                             headers=headers, params=parameters)
        # import pdb
        #
        # pdb.set_trace()
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_activate_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization}

        # The parameters of post_iceauth_api_v2_users_activate_helper
        parameters = {
            'uid': uid}

        # The request payload of post_iceauth_api_v2_users_activate_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/activate', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def get_iceauth_api_v2_users_anonymous_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_v2_users_anonymous_helper
        parameters = {
            'uid': uid}

        # The request payload of get_iceauth_api_v2_users_anonymous_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/anonymous', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_password_update_helper(self, newPassword=None, currPassword=None, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_v2_users_password_update_helper
        parameters = {
            'uid': uid}

        # The request payload of post_iceauth_api_v2_users_password_update_helper
        payload = {
            'newPassword': newPassword,
            'currPassword': currPassword}

        # Default values to be used
        # if not newPassword:
        #     payload['newPassword'] = INT_HOST[os.environ.get('ENV', 'newPassword')]
        #
        # if not currPassword:
        #     payload['currPassword'] = INT_HOST[os.environ.get('ENV', 'currPassword')]
        #
        # if not uid:
        #     parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/password/update', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/password/update, Response\n:{response}")
        return response

    def delete_iceauth_api_v2_users_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization}

        # The parameters of delete_iceauth_api_v2_users_helper
        parameters = {
            'uid': uid}

        # The request payload of delete_iceauth_api_v2_users_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.delete('ICEAUTH/api/v2/users', payload=payload, headers=headers,
                                                params=parameters)
        logger.info(f"ICEAUTH/api/v2/users, Response\n:{response}")
        return response

    def post_iceauth_api_v2_users_deactivate_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization}

        # The parameters of post_iceauth_api_v2_users_deactivate_helper
        parameters = {
            'uid': uid}

        # The request payload of post_iceauth_api_v2_users_deactivate_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/deactivate', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_json_password_reset_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_v2_users_json_password_reset_helper
        parameters = {
        }

        # The request payload of post_iceauth_api_v2_users_json_password_reset_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/json/password/reset', payload=payload,
                                              headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json/password/reset, Response\n:{response}")
        return response

    def get_iceauth_api_v2_users_find_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_v2_users_find_helper
        parameters = {
            'uid': uid}

        # The request payload of get_iceauth_api_v2_users_find_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/find', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def delete_iceauth_api_v2_users_json_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of delete_iceauth_api_v2_users_json_helper
        parameters = {
        }

        # The request payload of delete_iceauth_api_v2_users_json_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.delete('ICEAUTH/api/v2/users/json', payload=payload, headers=headers,
                                                params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def get_iceauth_api_v2_users_json_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of get_iceauth_api_v2_users_json_helper
        parameters = {
        }

        # The request payload of get_iceauth_api_v2_users_json_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/json', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def put_iceauth_api_v2_users_json_helper(self, userMetaData=None, uid=None, surname=None, preferredLanguage=None,
                                             organizationalUnit=None, mail=None, initials=None, givenName=None,
                                             commonName=None, cellN=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"
        person = generate_username()
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Content-Type': 'application/json',
            'Authorization': Authorization}

        # The parameters of post_iceauth_api_v2_users_json_helper
        parameters = {
        }

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

        # Default values to be used
        if not userMetaData:
            payload['userMetaData'] = INT_HOST[os.environ.get('ENV', 'userMetaData')]

        if not uid:
            payload['uid'] = person['name']

        if not surname:
            payload['surname'] = person['surname']

        if not preferredLanguage:
            payload['preferredLanguage'] = INT_HOST[os.environ.get('ENV', 'language')]

        if not organizationalUnit:
            payload['organizationalUnit'] = INT_HOST[os.environ.get('ENV', 'organizationalUnit')]

        if not mail:
            payload['mail'] = person['email']

        if not initials:
            payload['initials'] = INT_HOST[os.environ.get('ENV', 'initials')]

        if not givenName:
            payload['givenName'] = person['surname']

        if not commonName:
            payload['commonName'] = person['surname']

        if not cellN:
            payload['cellN'] = INT_HOST[os.environ.get('ENV', 'cellN')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.put('ICEAUTH/api/v2/users/json', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response\n:{response}")
        return response

    def get_iceauth_api_v2_users_json_anonymous_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of get_iceauth_api_v2_users_json_anonymous_helper
        parameters = {
        }

        # The request payload of get_iceauth_api_v2_users_json_anonymous_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/json/anonymous', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_json_anonymous_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_v2_users_json_anonymous_helper
        parameters = {
        }

        # The request payload of post_iceauth_api_v2_users_json_anonymous_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/json/anonymous', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_json_activate_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_v2_users_json_activate_helper
        parameters = {
        }

        # The request payload of post_iceauth_api_v2_users_json_activate_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/json/activate', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def get_iceauth_api_v2_users_json_find_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of get_iceauth_api_v2_users_json_find_helper
        parameters = {
        }

        # The request payload of get_iceauth_api_v2_users_json_find_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/json/find', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_json_lock_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_v2_users_json_lock_helper
        parameters = {
        }

        # The request payload of post_iceauth_api_v2_users_json_lock_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/json/lock', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_json_password_resetrequest_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': 'application/json',
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_v2_users_json_password_resetrequest_helper
        parameters = {
        }

        # The request payload of post_iceauth_api_v2_users_json_password_resetrequest_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/json/password/resetRequest', payload=payload,
                                              headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def get_iceauth_api_v2_users_userroles_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_v2_users_userroles_helper
        parameters = {
            'uid': uid}

        # The request payload of get_iceauth_api_v2_users_userroles_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/userRoles', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def get_iceauth_api_v2_users_search_helper(self, uid=None, addRoles=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*'}

        # The parameters of get_iceauth_api_v2_users_search_helper
        parameters = {
            'uid': uid,
            'addRoles': addRoles}

        # The request payload of get_iceauth_api_v2_users_search_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        if not addRoles:
            parameters['addRoles'] = INT_HOST[os.environ.get('ENV', 'addRoles')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.get('ICEAUTH/api/v2/users/search', payload=payload, headers=headers,
                                             params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_lock_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization}

        # The parameters of post_iceauth_api_v2_users_lock_helper
        parameters = {
            'uid': uid}

        # The request payload of post_iceauth_api_v2_users_lock_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/lock', payload=payload, headers=headers,
                                              params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response

    def post_iceauth_api_v2_users_json_password_update_helper(self, uid=None):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of post_iceauth_api_v2_users_json_password_update_helper
        parameters = {
        }

        # The request payload of post_iceauth_api_v2_users_json_password_update_helper
        payload = {
            'uid': uid}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        logger.info(
            f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
        response = self.requests_utility.post('ICEAUTH/api/v2/users/json/password/update', payload=payload,
                                              headers=headers, params=parameters)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response
