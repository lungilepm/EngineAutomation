import os
from configs.hosts_config import USER_INFO
import logging as logger
from tests.auth.test_token_controller import obj_auth


def GET_ICEAUTH_oauth_jwk_set_helper(self, ):
	Authorization = f"Bearer {self.post_iceauth_oauth_token_helper()['access_token']}"

	# The headers of the request 
	headers = {
	'Authorization':Authorization,	
	'compress_token':',true',	
	'Accept':',application/json'}


	# The parameters of GET_ICEAUTH_oauth_jwk_set_helper
	parameters = {
	}


	# The request payload of GET_ICEAUTH_oauth_jwk_set_helper
	payload = {
	}

	# Default values to be used
	
	logger.info(f"Helper function for ICEAUTH/oauth/jwk_set payload :{payload}")
	response = self.requests_utility.GET('ICEAUTH/oauth/jwk_set', payload=payload, headers=headers, params=parameters)
	return response

def test_GET_ICEAUTH_oauth_jwk_set():
	expected_assert = 'Listed results'
	logger.info("TEST: test GET  call: ICEAUTH/oauth/jwk_set")
	api_info = obj_auth.GET_ICEAUTH_oauth_jwk_set_helper()
	logger.debug(f"TEST: test GET call ICEAUTH/oauth/jwk_set return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
