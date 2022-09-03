import os

from configs.hosts_config import USER_INFO, INT_HOST

import logging as logger

from utilities.genericUtilities import generate_username
from utilities.requestsUtility import RequestsUtility


class AuthHelper(object):
    def __init__(self):
        self.requests_utility = RequestsUtility()

    def login_to_auth_helper(self, client_id=None, client_secret=None, grant_type=None,
                             otp=None, username=None, password=None, refresh_token=None, u_sub=None):

        payload = {
            'client_id': client_id,
            'client_secret': client_secret,
            'grant_type': grant_type,
            'username': username,
            'password': password,
            'refresh_token': refresh_token,
            'otp': otp,
            'uSub': u_sub
        }

        if not client_id:
            payload['client_id'] = USER_INFO[os.environ.get('ENV', 'client_id')]

        if not client_secret:
            payload['client_secret'] = USER_INFO[os.environ.get('ENV', 'client_secret')]

        if not grant_type:
            payload['grant_type'] = USER_INFO[os.environ.get('ENV', 'grant_type')]

        if not username:
            payload['username'] = INT_HOST[os.environ.get('ENV', 'username')]

        if not password:
            payload['password'] = INT_HOST[os.environ.get('ENV', 'password')]

        if not u_sub:
            payload['uSub'] = USER_INFO[os.environ.get('ENV', 'uSub')]
        logger.info(f"/ICEAUTH/oauth/token payload :{payload}")
        response = self.requests_utility.post('ICEAUTH/oauth/token', payload=payload)
        # import pdb
        # pdb.set_trace()
        return response

    def create_new_user_helper(self, cell_number=None, name=None, surname=None, email=None, initials=None,
                               organizational_unit=None, preferred_language=None, uid=None):
        temp = generate_username()
        auth = self.login_to_auth_helper()['access_token']
        logger.info(f"Generated username :{temp}")
        logger.debug(f"Auth token generated{auth}")
        # create payload
        payload = {
            'cellN': cell_number,
            'commonName': name,
            'givenName': name,
            'initials': initials,
            'mail': email,
            'organizationalUnit': organizational_unit,
            'preferredLanguage': preferred_language,
            'surname': surname,
            'uid': uid,
            'userMetaData': {}
        }
        if not cell_number:
            payload['cellN'] = USER_INFO[os.environ.get('ENV', 'cellN')]
        if not name:
            payload['commonName'] = temp['name']
            payload['givenName'] = temp['name']
            payload['uid'] = temp['name']
        if not email:
            payload['mail'] = temp['email']
        if not surname:
            payload['surname'] = temp['surname']
        if not initials:
            payload['initials'] = USER_INFO[os.environ.get('ENV', 'initials')]
        if not organizational_unit:
            payload['organizationalUnit'] = USER_INFO[os.environ.get('ENV', 'organizationalUnit')]
        if not preferred_language:
            payload['preferredLanguage'] = USER_INFO[os.environ.get('ENV', 'preferredLanguage')]
        if not initials:
            payload['initials'] = USER_INFO[os.environ.get('ENV', 'initials')]
        logger.debug(f"The payload of 'test_create_new_user()'  {payload}")
        response = self.requests_utility.post(endpoint='ICEAUTH/api/v2/users/json', payload=payload, auth=auth)

        return response
