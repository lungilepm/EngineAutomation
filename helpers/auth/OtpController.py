from helpers.auth.TokenController import TokenController
from utilities.requestsUtility import RequestsUtility
from configs.hosts_config import INT_HOST
import logging as logger
from tests.auth.test_token_controller import obj_auth


class OtpController(object):

    def __init__(self):
        self.requests_utility = RequestsUtility()
        self.token_controller = TokenController()
        self.userName = []

    def iceauth_rest_v1_otp_send_helper(self, uuid=None, subject=None, requestUser=None, requestPassword=None,
                                        message=None, msisdn=None, mail=None, statusCode =200):
        Authorization = f"Bearer {self.token_controller.post_iceauth_oauth_token_helper()['access_token']}"

        # The headers of the request
        headers = {
            'Authorization': Authorization,
            'Accept': '*/*',
            'Content-Type': 'application/json'}

        # The parameters of iceauth_rest_v1_otp_send_helper
        parameters = {
        }

        # The request payload of iceauth_rest_v1_otp_send_helper
        payload = {
            'uuid': uuid,
            'subject': subject,
            'requestUser': requestUser,
            'requestPassword': requestPassword,
            'message': message,
            'msisdn': msisdn,
            'mail': mail}

        # Default values to be used

        logger.info(f"Helper function for iceauth/api/v2/users/json \npayload :\n\t{payload}\nparams :\n\t{parameters}\nheaders :\n\t{headers}")
        response = self.requests_utility.post('ICEAUTH/rest/v1/otp/send', payload=payload, headers=headers,
                                              params=parameters, expected_status_code=statusCode)
        logger.info(f"ICEAUTH/api/v2/users/json, Response {response}")
        return response
