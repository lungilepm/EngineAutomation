import pytest
import uuid as uuid

from helpers.auth.OtpController import OtpController
from utilities.genericUtilities import *
from helpers.auth.UserControllerV2 import UserControllerV2

obj_roles = UserControllerV2()
obj_auth = OtpController()

int_rand = random.randint(0, 999999)

requestUser = INT_HOST[os.environ.get('ENV', 'username')]
msisdn = INT_HOST[os.environ.get('ENV', 'cellN')]
mail = INT_HOST[os.environ.get('ENV', 'mail')]

list_of_username = {requestUser, None, "yout"}
list_of_UUID = {uuid, None, }
list_of_email = {mail, None, "emailnotknown@notin.com"}
list_of_msidn = {msisdn, None, "0740404040"}
list_of_subject = {f"otp automation subject ", None}
list_of_Message = {f"$otp automation message ", None}


@pytest.mark.parametrize("username", list_of_username)
@pytest.mark.parametrize("email", list_of_email)
@pytest.mark.parametrize("msisdn", list_of_msidn)
def test_iceauth_rest_v1_otp_send(caplog, username, email, msisdn):
    status_code_expected = 200

    expected_assert = 'Listed results'
    uuid_ = str(uuid.uuid4())
    logger.info("TEST: test post  call: ICEAUTH/rest/v1/otp/send")
    with caplog.at_level(logger.DEBUG):
        api_info = obj_auth.iceauth_rest_v1_otp_send_helper(requestUser=username, uuid=uuid_, mail=email, msisdn=msisdn,
                                                            subject=f"Automation Script subject {int_rand}",
                                                            message=f"$otp automation message  {int_rand}",
                                                            statusCode=status_code_expected)
    logger.info(f"TEST: test post call ICEAUTH/rest/v1/otp/send return payload: {api_info}")
    # actual_result = api_info['message']
    # assert expected_assert == actual_result, f"test failed to assert positive"
    # f"Expected assert: {expected_assert} but actual: {actual_result}"
