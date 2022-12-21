import os
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility
from configs.hosts_config import INT_HOST
import logging as logger
from tests.auth.test_token_controller import obj_auth


def get_iceauth_api_users_getusersforagency_0_helper(self, unallocated=None,includeChildren=None):
	Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

	# The headers of the request 
	headers = {
	'Authorization':Authorization,	
	'Accept':'*/*'}


	# The parameters of get_iceauth_api_users_getusersforagency_0_helper
	parameters = {
	'unallocated':unallocated,	
	'includeChildren':includeChildren}


	# The request payload of get_iceauth_api_users_getusersforagency_0_helper
	payload = {
	}

	# Default values to be used
	if not unallocated:
 		parameters['unallocated'] = INT_HOST[os.environ.get('ENV', 'unallocated')]
	
	if not includeChildren:
 		parameters['includeChildren'] = INT_HOST[os.environ.get('ENV', 'includeChildren')]
	
	
	logger.info(f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
	response = self.requests_utility.get('ICEAUTH/api/users/getUsersForAgency/0', payload=payload, headers=headers, params=parameters)
	logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
	return response

def test_get_iceauth_api_users_getusersforagency_0(caplog):
	expected_assert = 'Listed results'
	logger.info("TEST: test get  call: ICEAUTH/api/users/getUsersForAgency/0")
	api_info = obj_auth.get_iceauth_api_users_getusersforagency_0_helper()
	logger.debug(f"TEST: test get call ICEAUTH/api/users/getUsersForAgency/0 return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
	f"TEST:test get call ICEAUTH/api/users/getUsersForAgency/0 return payload:{api_info}") 
	assert expected_assert in api_info[0], f"test failed to assert positive"
	f"Expected assert:{expected_assert} but actual does not exist"