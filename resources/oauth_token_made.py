import os
from configs.hosts_config import USER_INFO
import logging as logger
from tests.auth.test_token_controller import obj_auth


def post_iceauth_api_v2_users_json_helper(self, userMetaData=None,uid=None,surname=None,preferredLanguage=None,organizationalUnit=None,mail=None,initials=None,givenName=None,commonName=None,cellN=None):
	auth = self.post_iceauth_oauth_token_helper()['access_token']
	bearer_auth = f'Bearer {auth}'

	# The headers of the request 
	headers ={'authorization': 'bearer_auth', 'compress_token': 'true', 'content-type': 'application/json'}

	# The request payload of post_iceauth_api_v2_users_json_helper
	payload = {
	'userMetaData':userMetaData,	
	'uid':uid,	
	'surname':surname,	
	'preferredLanguage':preferredLanguage,	
	'organizationalUnit':organizationalUnit,	
	'mail':mail,	
	'initials':initials,	
	'givenName':givenName,	
	'commonName':commonName,	
	'cellN':cellN}

	# Default values to be used
	if not userMetaData:
 		payload['userMetaData'] = INT_HOST[os.environ.get('ENV', 'userMetaData')]
	
	if not uid:
 		payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]
	
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
 		payload['givenName'] = INT_HOST[os.environ.get('ENV', 'givenName')]
	
	if not commonName:
 		payload['commonName'] = INT_HOST[os.environ.get('ENV', 'commonName')]
	
	if not cellN:
 		payload['cellN'] = INT_HOST[os.environ.get('ENV', 'cellN')]
	
	
	logger.info(f"Helper function for iceauth/api/v2/users/json payload :{payload}")
	response = self.requests_utility.post('iceauth/api/v2/users/json', payload=payload, headers=headers, auth=auth)
	return response

def test_post_iceauth_api_v2_users_json():
	expected_assert = 'Listed results'
	logger.info("TEST: test post  call: iceauth/api/v2/users/json")
	api_info = obj_auth.post_iceauth_api_v2_users_json_helper()
	logger.debug(f"TEST: test that a post can access iceauth/api/v2/users/json return payload {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
