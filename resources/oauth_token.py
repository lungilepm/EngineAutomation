import os
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility
from configs.hosts_config import INT_HOST
import logging as logger
from tests.auth.test_token_controller import obj_auth


def iceauth_oauth_token_helper(self, uSub=None,otp=None,refresh_token=None,password=None,username=None,grant_type=None,client_secret=None,client_id=None):
	Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

	# The headers of the request 
	headers = {
	'compress_token':'true',	
	'realm':'/ke/ntsa/int',	
	'Accept':'*/*',	
	'Content-Type':'application/json'}


	# The parameters of iceauth_oauth_token_helper
	parameters = {
	}


	# The request payload of iceauth_oauth_token_helper
	payload = {
	'uSub':uSub,	
	'otp':otp,	
	'refresh_token':refresh_token,	
	'password':password,	
	'username':username,	
	'grant_type':grant_type,	
	'client_secret':client_secret,	
	'client_id':client_id}

	# Default values to be used
	if not uSub:
 		payload['uSub'] = INT_HOST[os.environ.get('ENV', 'uSub')]
	
	if not otp:
 		payload['otp'] = INT_HOST[os.environ.get('ENV', 'otp')]
	
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
	
	
	logger.info(f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
	response = self.requests_utility.iceauth/oauth/token('ICEAUTH/oauth/token', payload=payload, headers=headers, params=parameters)
	logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
	return response

def test_iceauth_oauth_token(caplog):
	expected_assert = 'Listed results'
	logger.info("TEST: test iceauth/oauth/token  call: ICEAUTH/oauth/token")
	api_info = obj_auth.iceauth_oauth_token_helper()
	logger.info(f"TEST: test iceauth/oauth/token call ICEAUTH/oauth/token return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
	f"TEST:test get call ICEAUTH/oauth/token return payload:{api_info}") 
	assert expected_assert in api_info[0], f"test failed to assert positive"
	f"Expected assert:{expected_assert} but actual does not exist"