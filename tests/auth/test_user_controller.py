import os
import logging as logger
from configs.hosts_config import INT_HOST
from helpers.auth.TokenController import TokenController
from helpers.auth.UserController import UserController

obj_auth = UserController()
login_check = TokenController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]
role_path = INT_HOST[os.environ.get('ENV', 'roles_path')]


def test_get_iceauth_api_users_getusersforagency(caplog):
    caplog.set_level(logger.INFO)
    expected_assert = 'uid'
    logger.info("TEST: test get  call: ICEAUTH/api/users/getUsersForAgency/0")
    api_info = obj_auth.get_iceauth_api_users_getusersforagency_helper()
    logger.debug(f"TEST: test get call ICEAUTH/api/users/getUsersForAgency/0 return payload: {api_info[0]}")
    assert expected_assert in api_info[0], f"test failed to assert positive" \
                                           f"Expected assert:{expected_assert} but actual does not exist"

