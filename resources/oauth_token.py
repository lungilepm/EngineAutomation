import os
from configs.hosts_config import USER_INFO
import logging as logger
from tests.auth.test_token_controller import obj_auth


def post_iceauth_api_roles_json_addusertorole_helper(self, uid=None,,agencyId=None,,roleName=None):
	Authorization = f"Bearer {self.post_iceauth_oauth_token_helper()['access_token']}"

	# The headers of the request 
	headers = {
	'Authorization':Authorization,	
	'Accept':'*/*',	
	'Content-Type':'application/json'}


	# The parameters of post_iceauth_api_roles_json_addusertorole_helper
	parameters = {
	}


	# The request payload of post_iceauth_api_roles_json_addusertorole_helper
	payload = {
	'uid':uid,	
	'agencyId':agencyId,	
	'roleName':roleName}

	# Default values to be used
	if not uid:
 		payload['uid'] = INT_HOST[os.environ.get('ENV', 'uid')]
	
	if not agencyId:
 		payload['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]
	
	if not roleName:
 		payload['roleName'] = INT_HOST[os.environ.get('ENV', 'roleName')]
	
	
	logger.info(f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
	response = self.requests_utility.post('ICEAUTH/api/roles/json/addUserToRole', payload=payload, headers=headers, params=parameters)
	return response

def test_post_iceauth_api_roles_json_addusertorole():
	expected_assert = 'Listed results'
	logger.info("TEST: test post  call: ICEAUTH/api/roles/json/addUserToRole")
	api_info = obj_auth.post_iceauth_api_roles_json_addusertorole_helper()
	logger.debug(f"TEST: test post call ICEAUTH/api/roles/json/addUserToRole return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
