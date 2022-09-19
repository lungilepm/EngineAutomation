import os
import logging as logger
from configs.hosts_config import INT_HOST
from utilities.genericUtilities import generate_username
from utilities.requestsUtility import RequestsUtility


class AuthHelper(object):
    def __init__(self):
        self.requests_utility = RequestsUtility()

    # region _____________________________________TOKEN_CONTROLLER_______________________________________________________________
    def post_iceauth_oauth_token_helper(self, uSub=None, otp=None, refresh_token=None, password=None, username=None,
                                        grant_type=None, client_secret=None, client_id=None):

        # The headers of the request
        headers = {'compress_token': 'true', 'content-type': 'application/json', 'Accept': '*/*'}

        # The request payload of post_iceauth_oauth_token_helper
        payload = {
            'uSub': uSub,
            'otp': otp,
            'refresh_token': refresh_token,
            'password': password,
            'username': username,
            'grant_type': grant_type,
            'client_secret': client_secret,
            'client_id': client_id}

        # Default values to be used
        # if not uSub:
        #     payload['uSub'] = INT_HOST[os.environ.get('ENV', 'uSub')]

        # if not otp:
        #     payload['otp'] = INT_HOST[os.environ.get('ENV', 'otp')]

        if not refresh_token:
            payload['refresh_token'] = INT_HOST[os.environ.get('ENV', 'refresh_token')]

        if not password:
            payload['password'] = INT_HOST[os.environ.get('ENV', 'password')]

        if not username:
            payload['username'] = INT_HOST[os.environ.get('ENV', 'username')]

        if not grant_type:
            payload['grant_type'] = INT_HOST[os.environ.get('ENV', 'grant_type')]

        if not client_secret:
            payload['client_secret'] = INT_HOST[os.environ.get('ENV', 'client_secret')]

        if not client_id:
            payload['client_id'] = INT_HOST[os.environ.get('ENV', 'client_id')]

        logger.info(f"Helper function for iceauth/oauth/token payload :{payload}")
        response = self.requests_utility.post('iceauth/oauth/token', payload=payload, headers=headers)
        return response

    # endregion
    def post_iceauth_api_v2_users_json_helper(self, userMetaData=None, uid=None, surname=None, preferredLanguage=None,
                                              organizationalUnit=None, mail=None, initials=None, givenName=None,
                                              commonName=None, cellN=None):
        temp = generate_username()
        auth = self.post_iceauth_oauth_token_helper()['access_token']
        bearer_auth = f'Bearer {auth}'

        # The headers of the request
        headers = {'authorization': bearer_auth, 'compress_token': 'true', 'content-type': 'application/json'}

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

        logger.info(f"Helper function for iceauth/api/v2/users/json payload :{payload}")
        response = self.requests_utility.post('iceauth/api/v2/users/json', payload=payload, headers=headers)
        return response

    def get_iceauth_api_v2_users_json_helper(self, uid=None, newPassword=None, currPassword=None):
        auth = self.post_iceauth_oauth_token_helper()['access_token']
        bearer_auth = f'Bearer {auth}'

        # The headers of the request
        headers = {'content-type': 'application/json', 'accept': '*/*', 'Authorization': bearer_auth}

        # The request payload of get_iceauth_api_v2_users_json_helper
        payload = {
            'uid': uid,
            'newPassword': newPassword,
            'currPassword': currPassword}

        # Default values to be used
        if not uid:
            payload['uid'] = INT_HOST[os.environ.get('ENV', 'username')]

        # if not newPassword:
        #     payload['newPassword'] = INT_HOST[os.environ.get('ENV', 'newPassword')]
        #
        # if not currPassword:
        #     payload['currPassword'] = INT_HOST[os.environ.get('ENV', 'currPassword')]

        logger.info(f"Helper function for iceauth/api/v2/users/json payload :{payload}")
        response = self.requests_utility.get('iceauth/api/v2/users/json', payload=payload, headers=headers)
        return response

    def get_iceauth_api_realms_helper(self):
        auth = self.post_iceauth_oauth_token_helper()['access_token']
        bearer_auth = f'Bearer {auth}'

        # The headers of the request
        headers = {'accept': '*/*'}

        # The request payload of get_iceauth_api_realms_helper
        payload = {
        }

        # Default values to be used

        logger.info(f"Helper function for iceauth/api/realms payload :{payload}")
        response = self.requests_utility.get('iceauth/api/realms', payload=payload, headers=headers)
        return response

    def post_iceauth_oauth_token_helper_2(self, password=None, username=None, client_secret=None, client_id=None,
                                          grant_type=None):
        authorization = self.post_iceauth_oauth_token_helper()['access_token']

        # The headers of the request
        headers = {
            'realm': 'realm',
            'origin': 'origin',
            'content-type': 'content-type',
            'compress_token': 'compress_token',
            'accept': 'accept'}

        # The parameters of post_iceauth_oauth_token_helper
        parameters = {
            'password': password,
            'username': username,
            'client_secret': client_secret,
            'client_id': client_id,
            'grant_type': grant_type}

        # The request payload of post_iceauth_oauth_token_helper
        payload = {
        }

        # Default values to be used
        if not password:
            parameters['password'] = INT_HOST[os.environ.get('ENV', 'password')]

        if not username:
            parameters['username'] = INT_HOST[os.environ.get('ENV', 'username')]

        if not client_secret:
            parameters['client_secret'] = INT_HOST[os.environ.get('ENV', 'client_secret')]

        if not client_id:
            parameters['client_id'] = INT_HOST[os.environ.get('ENV', 'client_id')]

        if not grant_type:
            parameters['grant_type'] = INT_HOST[os.environ.get('ENV', 'grant_type')]

        logger.info(f"Helper function for iceauth/oauth/token payload :{payload}")
        response = self.requests_utility.post('ICEAUTH/oauth/token', payload=payload, headers=headers,
                                              params=parameters, expected_status_code=500)
        return response

    def get_iceauth_api_roles_getallroles_helper(self, agencyId=None):
        Authorization = f"Bearer {self.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': ',*/*'}

        # The parameters of get_iceauth_api_roles_getallroles_helper
        parameters = {
            'agencyId': agencyId}

        # The request payload of get_iceauth_api_roles_getallroles_helper
        payload = {
        }

        # Default values to be used
        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(f"Helper function for ICEAUTH/api/roles/getAllRoles payload :{payload}")
        response = self.requests_utility.get('ICEAUTH/api/roles/getAllRoles', payload=payload, headers=headers,
                                             params=parameters)
        return response

    def post_iceauth_api_roles_addusertorole_helper(self, uid=None, roleName=None, clearCache=None, agencyId=None):
        Authorization = f"Bearer {self.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization}

        # The parameters of post_iceauth_api_roles_addusertorole_helper
        parameters = {
            'uid': uid,
            'roleName': roleName,
            'clearCache': clearCache,
            'agencyId': agencyId}

        # The request payload of post_iceauth_api_roles_addusertorole_helper
        payload = {
        }

        # Default values to be used
        if not uid:
            parameters['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]

        if not roleName:
            parameters['roleName'] = INT_HOST[os.environ.get('ENV', 'roleName')]

        if not clearCache:
            parameters['clearCache'] = True

        if not agencyId:
            parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]

        logger.info(f"Helper function for ICEAUTH/api/roles/addUserToRole payload :{payload}")
        response = self.requests_utility.post('ICEAUTH/api/roles/addUserToRole', payload=payload, headers=headers,
                                              params=parameters, expected_status_code=201)
        return response
