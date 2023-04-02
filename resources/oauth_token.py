import os
from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility
from configs.hosts_config import INT_HOST
import logging as logger
from tests.auth.test_token_controller import obj_auth


def iceauth_rest_v1_otp_send_helper(self, uuid=None,subject=None,requestUser=None,requestPassword=None,message=None,msisdn=None,mail=None):
	Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

	# The headers of the request 
	headers = {
	'Authorization':Authorization,	
	'Accept':'*/*',	
	'Content-Type':'application/json'}


	# The parameters of iceauth_rest_v1_otp_send_helper
	parameters = {
	}


	# The request payload of iceauth_rest_v1_otp_send_helper
	payload = {
	'uuid':uuid,	
	'subject':subject,	
	'requestUser':requestUser,	
	'requestPassword':requestPassword,	
	'message':message,	
	'msisdn':msisdn,	
	'mail':mail}

	# Default values to be used
	if not uuid:
 		payload['uuid'] = INT_HOST[os.environ.get('ENV', 'uuid')]
	
	if not subject:
 		payload['subject'] = INT_HOST[os.environ.get('ENV', 'subject')]
	
	if not requestUser:
 		payload['requestUser'] = INT_HOST[os.environ.get('ENV', 'requestUser')]
	
	if not requestPassword:
 		payload['requestPassword'] = INT_HOST[os.environ.get('ENV', 'requestPassword')]
	
	if not message:
 		payload['message'] = INT_HOST[os.environ.get('ENV', 'message')]
	
	if not msisdn:
 		payload['msisdn'] = INT_HOST[os.environ.get('ENV', 'msisdn')]
	
	if not mail:
 		payload['mail'] = INT_HOST[os.environ.get('ENV', 'mail')]
	
	
	logger.info(f"Helper function for iceauth/api/v2/users/json Authentication: {Authorization}\npayload :{payload}\nparams :{parameters}\nheaders :{headers}")
	response = self.requests_utility.post('ICEAUTH/rest/v1/otp/send', payload=payload, headers=headers,
										  params=parameters)
	logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
	return response

def test_iceauth_rest_v1_otp_send(caplog):
	expected_assert = 'Listed results'
	logger.info("TEST: test post  call: ICEAUTH/rest/v1/otp/send")
	api_info = obj_auth.iceauth_rest_v1_otp_send_helper()
	logger.info(f"TEST: test post call ICEAUTH/rest/v1/otp/send return payload: {api_info}")
	actual_result = api_info['message']
	assert expected_assert == actual_result, f"test failed to assert positive"
	f"Expected assert: {expected_assert} but actual: {actual_result}"
	f"TEST:test get call ICEAUTH/rest/v1/otp/send return payload:{api_info}") 
	assert expected_assert in api_info[0], f"test failed to assert positive"
	f"Expected assert:{expected_assert} but actual does not exist"