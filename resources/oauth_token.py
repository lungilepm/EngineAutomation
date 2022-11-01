import os
from configs.hosts_config import INT_INFO
import logging as logger
from tests.auth.test_token_controller import obj_auth


def get_engine_rest_requestservice_helper(self, lookupDefinitionId=None,language=None,gatAgencyId=None,agencyId=None,serviceCode=None):
	Authorization = f"Bearer {self.post_iceauth_oauth_token_helper()['access_token']}"

	# The headers of the request 
	headers = {
	'Authorization':Authorization,	
	'Accept':'application/json;charset=UTF-8',	
	'Content-Type':'application/json'}


	# The parameters of get_engine_rest_requestservice_helper
	parameters = {
	'lookupDefinitionId':lookupDefinitionId,	
	'language':language,	
	'gatAgencyId':gatAgencyId,	
	'agencyId':agencyId,	
	'serviceCode':serviceCode}


	# The request payload of get_engine_rest_requestservice_helper
	payload = {
	}

	# Default values to be used
	if not lookupDefinitionId:
 		parameters['lookupDefinitionId'] = INT_HOST[os.environ.get('ENV', 'lookupDefinitionId')]
	
	if not language:
 		parameters['language'] = INT_HOST[os.environ.get('ENV', 'language')]
	
	if not gatAgencyId:
 		parameters['gatAgencyId'] = INT_HOST[os.environ.get('ENV', 'gatAgencyId')]
	
	if not agencyId:
 		parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]
	
	if not serviceCode:
 		parameters['serviceCode'] = INT_HOST[os.environ.get('ENV', 'serviceCode')]
	
	
	logger.info(f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
	response = self.requests_utility.get('ENGINE/rest/requestservice', payload=payload, headers=headers, params=parameters)
	return response

def test_get_engine_rest_requestservice():
	expected_assert = 'Listed results'
	logger.info("TEST: test get  call: ENGINE/rest/requestservice")
	api_info = obj_auth.get_engine_rest_requestservice_helper()
	logger.debug(f"TEST: test get call ENGINE/rest/requestservice return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
	f"TEST:test get call ENGINE/rest/requestservice return payload:{api_info}") 
	assert expected_assert in api_info[0], f"test failed to assert positive"
	f"Expected assert:{expected_assert} but actual does not exist"