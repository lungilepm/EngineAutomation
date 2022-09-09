import os
from configs.hosts_config import USER_INFO
import logging as logger
from tests.auth.test_token_controller import obj_auth


def post_iceauth_oauth_token_helper(self, password=None,username=None,client_secret=None,client_id=None,grant_type=None):
	auth = self.post_iceauth_oauth_token_helper()['access_token']
	bearer_auth = f'Bearer {auth}'

	# The headers of the request 
	headers ={'compress_token': 'true', 'accept': 'application/json', 'content-type': 'application/x-www-form-urlencoded', 'origin': 'http', 'realm': '/spsi/ice/int'}

	# The parameters of post_iceauth_oauth_token_helper
	parameters = {
	'password':password,	
	'username':username,	
	'client_secret':client_secret,	
	'client_id':client_id,	
	'grant_type':grant_type,	
	}


	# The request payload of post_iceauth_oauth_token_helper
	payload = {
	}

	# Default values to be used
	if not password:
 		payload['password'] = INT_HOST[os.environ.get('ENV', 'password')]
	
	if not username:
 		payload['username'] = INT_HOST[os.environ.get('ENV', 'username')]
	
	if not client_secret:
 		payload['client_secret'] = INT_HOST[os.environ.get('ENV', 'client_secret')]
	
	if not client_id:
 		payload['client_id'] = INT_HOST[os.environ.get('ENV', 'client_id')]
	
	if not grant_type:
 		payload['grant_type'] = INT_HOST[os.environ.get('ENV', 'grant_type')]
	
	
	logger.info(f"Helper function for iceauth/oauth/token payload :{payload}")
	response = self.requests_utility.post('iceauth/oauth/token', payload=payload, headers=headers, params=parameters, auth=auth)
	return response

def test_post_iceauth_oauth_token():
	expected_assert = 'Listed results'
	logger.info("TEST: test post  call: iceauth/oauth/token")
	api_info = obj_auth.post_iceauth_oauth_token_helper()
	logger.debug(f"TEST: test post call iceauth/oauth/token return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
