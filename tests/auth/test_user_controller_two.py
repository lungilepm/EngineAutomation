import pytest

from helpers.auth.TokenController import TokenController
from helpers.auth.UserControllerV2 import UserControllerV2
from utilities.genericUtilities import *

obj_auth = UserControllerV2()
login_check = TokenController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]
role_path = INT_HOST[os.environ.get('ENV', 'roles_path')]


def test_get_iceauth_api_v2_users(caplog, user):
    caplog.set_level(logger.INFO)
    expected_assert = 'authorities'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users")
    api_info = obj_auth.get_iceauth_api_v2_users_helper(uid=user['username'])
    logger.debug(f"TEST: test get call ICEAUTH/api/v2/users return payload: {api_info}")
    assert expected_assert in api_info[0], f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"


@pytest.mark.first
def test_post_iceauth_api_v2_users_json(caplog):
    caplog.set_level(logger.INFO)
    expected_assert = 'User created'
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json")
    api_info = obj_auth.post_iceauth_api_v2_users_json_helper()
    logger.debug(f"TEST: test post call ICEAUTH/api/v2/users/json return payload: {api_info}")
    password = api_info['data'][0]['userPassword']
    name = api_info['data'][0]['uid']
    actual_assert = api_info['message']
    assert expected_assert == actual_assert, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_assert}"
    f"TEST:test get call ICEAUTH/api/v2/users/activate return payload:{api_info}"
    written = {'username': name, 'password': password}


@pytest.mark.second
def test_get_iceauth_api_v2_users_json_getusersforagency(caplog):
    caplog.set_level(logger.INFO)

    expected_assert = 'Listed Users'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users/json/getUsersForAgency")
    api_info = obj_auth.get_iceauth_api_v2_users_json_getusersforagency_helper()
    logger.debug(f"TEST: test get call ICEAUTH/api/v2/users/json/getUsersForAgency return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_post_iceauth_api_v2_users_password_update(user, caplog):
    caplog.set_level(logger.INFO)
    expected_assert = username = user['username']
    # import pdb
    #
    # pdb.set_trace()
    password = obj_auth.post_iceauth_api_v2_users_json_password_reset_helper(uid=username)['data'][0]['pwd']
    api_info = obj_auth.post_iceauth_api_v2_users_password_update_helper(uid=username, newPassword=username,
                                                                         currPassword=password)
    logger.debug(f"TEST: test post call ICEAUTH/api/v2/users/password/update return payload: {api_info}")
    login = login_check.post_iceauth_oauth_token_helper(username=username, password=username)['username']
    logger.debug(f"Test login result: {login}")
    assert expected_assert == login, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {login}"
    f"TEST:test get call ICEAUTH/api/v2/users/activate return payload:{api_info}"


def test_post_iceauth_api_v2_users_json_password_reset(user, caplog):
    caplog.set_level(logger.INFO)
    expected_assert = 'Password Reset'
    user_name = user['username']
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json/password/reset")
    api_info = obj_auth.post_iceauth_api_v2_users_json_password_reset_helper(uid=user_name)
    logger.debug(f"TEST: test post call ICEAUTH/api/v2/users/json/password/reset return payload: {api_info}")
    actual_assert = api_info['message']
    assert expected_assert == actual_assert, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_assert}"
    f"TEST:test get call ICEAUTH/api/v2/users/activate return payload:{api_info}"


def test_delete_iceauth_api_v2_users(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    # import pdb
    #
    # pdb.set_trace()
    expected_assert = f"User : {name} was not found"
    logger.info("TEST: test delete  call: ICEAUTH/api/v2/users")
    api_info = obj_auth.delete_iceauth_api_v2_users_helper(uid=name)
    logger.debug(f"TEST: test delete call ICEAUTH/api/v2/users return payload: {api_info}")
    actual_result = obj_auth.get_iceauth_api_v2_users_helper(uid=name, expected_code=400)['error_detail']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"

    # import pdb
    #
    # pdb.set_trace()


def test_delete_iceauth_api_v2_users_json(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'User deleted'
    logger.info("TEST: test delete  call: ICEAUTH/api/v2/users/json")
    api_info = obj_auth.delete_iceauth_api_v2_users_json_helper(uid=name)
    logger.debug(f"TEST: test delete call ICEAUTH/api/v2/users/json return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/json return payload:{api_info}"
