import logging as logger
import os

from tests.auth.test_token_controller import obj_auth


def get_engine_rest_activity_loadlistactivitymetadata_helper(self, language=None,agencyId=None,activityCd=None):
	Authorization = f"Bearer {self.post_iceauth_oauth_token_helper()['access_token']}"

	# The headers of the request 
	headers = {
	'Authorization':Authorization,	
	'Accept':'application/json'}


	# The parameters of get_engine_rest_activity_loadlistactivitymetadata_helper
	parameters = {
	'language':language,	
	'agencyId':agencyId,	
	'activityCd':activityCd}


	# The request payload of get_engine_rest_activity_loadlistactivitymetadata_helper
	payload = {
	}

	# Default values to be used
	if not language:
 		parameters['language'] = INT_HOST[os.environ.get('ENV', 'language')]
	
	if not agencyId:
 		parameters['agencyId'] = INT_HOST[os.environ.get('ENV', 'agencyId')]
	
	if not activityCd:
 		parameters['activityCd'] = INT_HOST[os.environ.get('ENV', 'activityCd')]
	
	
	logger.info(f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
	response = self.requests_utility.get('ENGINE/rest/activity/loadListActivityMetaData', payload=payload, headers=headers, params=parameters)
	return response

def test_get_engine_rest_activity_loadlistactivitymetadata():
	expected_assert = 'Listed results'
	logger.info("TEST: test get  call: ENGINE/rest/activity/loadListActivityMetaData")
	api_info = obj_auth.get_engine_rest_activity_loadlistactivitymetadata_helper()
	logger.debug(f"TEST: test get call ENGINE/rest/activity/loadListActivityMetaData return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
	f"TEST:test get call ENGINE/rest/activity/loadListActivityMetaData return payload:{api_info}") 
	assert expected_assert in api_info[0], f"test failed to assert positive"
	f"Expected assert:{expected_assert} but actual does not exist"