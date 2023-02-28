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


def test_get_iceauth_api_v2_users_json_getusersforagency(caplog):
    caplog.set_level(logger.INFO)

    expected_assert = 'Listed Users'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users/json/getUsersForAgency")
    api_info = obj_auth.get_iceauth_api_v2_users_json_getusersforagency_helper()
    logger.debug(f"TEST: test get call ICEAUTH/api/v2/users/json/getUsersForAgency return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_post_iceauth_api_v2_users_activate(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 200
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/activate")
    api_info = obj_auth.post_iceauth_api_v2_users_activate_helper(uid=name)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/activate return payload: {api_info}")
    actual_result = api_info['statusCode']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_post_iceauth_api_v2_users_password_update(user, caplog):
    caplog.set_level(logger.INFO)
    expected_assert = username = user['username']
    newPassword = generate_username()['name']
    password = obj_auth.post_iceauth_api_v2_users_json_password_reset_helper(uid=username)['data'][0]['pwd']
    api_info = obj_auth.post_iceauth_api_v2_users_password_update_helper(uid=username, newPassword=newPassword,
                                                                         currPassword=password)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/password/update return payload: {password}")
    login = login_check.post_iceauth_oauth_token_helper(username=username, password=newPassword)['username']
    logger.info(f"Test login result: {login}")
    # import pdb
    #
    # pdb.set_trace()

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
    api_info = obj_auth.delete_iceauth_api_v2_users_helper(uid=name)
    logger.info(f"TEST: test delete call ICEAUTH/api/v2/users return payload: {api_info}")
    actual_result = obj_auth.get_iceauth_api_v2_users_helper(uid=name)['error_detail']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


# import pdb
#
# pdb.set_trace()


def test_post_iceauth_api_v2_users_deactivate(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 200
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/deactivate")
    api_info = obj_auth.post_iceauth_api_v2_users_deactivate_helper(uid=name)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/deactivate return payload: {api_info}")
    actual_result = api_info['statusCode']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_delete_iceauth_api_v2_users_json(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'User deleted'
    logger.info("TEST: test delete  call: ICEAUTH/api/v2/users/json")
    api_info = obj_auth.delete_iceauth_api_v2_users_json_helper(uid=name)
    logger.info(f"TEST: test delete call ICEAUTH/api/v2/users/json return payload: {api_info}")
    actual_result = api_info['message']


def test_get_iceauth_api_v2_users_json(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'surname'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users/json")
    api_info = obj_auth.get_iceauth_api_v2_users_json_helper(uid=name)
    # import pdb
    #
    # pdb.set_trace()
    logger.info(f"TEST: test get call ICEAUTH/api/v2/users/json return payload: {api_info}")
    actual_result = api_info["data"][0]

    assert expected_assert in actual_result, f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"


def test_put_iceauth_api_v2_users_json(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'User updated'
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json")
    api_info = obj_auth.put_iceauth_api_v2_users_json_helper(uid=name)
    logger.debug(f"TEST: test post call ICEAUTH/api/v2/users/json return payload: {api_info}")
    password = api_info['data'][0]['userPassword']
    name = api_info['data'][0]['uid']
    actual_assert = api_info['message']
    # import pdb
    #
    # pdb.set_trace()
    assert expected_assert == actual_assert, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_assert}"
    f"TEST:test get call ICEAUTH/api/v2/users/activate return payload:{api_info}"
    written = {'username': name, 'password': password}


def test_get_iceauth_api_v2_users_json_anonymous(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'Listed results'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users/json/anonymous")
    api_info = obj_auth.get_iceauth_api_v2_users_json_anonymous_helper(uid=name)
    logger.info(f"TEST: test get call ICEAUTH/api/v2/users/json/anonymous return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/json/anonymous return payload:{api_info}"


def test_post_iceauth_api_v2_users_json_anonymous(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'Listed results'
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json/anonymous")
    api_info = obj_auth.post_iceauth_api_v2_users_json_anonymous_helper(uid=name)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/json/anonymous return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/json/anonymous return payload:{api_info}"


def test_post_iceauth_api_v2_users_json_activate(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'User activated'
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json/activate")
    api_info = obj_auth.post_iceauth_api_v2_users_json_activate_helper(uid=name)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/json/activate return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/json/activate return payload:{api_info}"


def test_get_iceauth_api_v2_users_json_find(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'Listed results'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users/json/find")
    api_info = obj_auth.get_iceauth_api_v2_users_json_find_helper(uid=name)
    logger.info(f"TEST: test get call ICEAUTH/api/v2/users/json/find return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/json/find return payload:{api_info}"


def test_post_iceauth_api_v2_users_json_lock(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'User locked'
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json/lock")
    api_info = obj_auth.post_iceauth_api_v2_users_json_lock_helper(uid=name)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/json/lock return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/json/lock return payload:{api_info}"


def test_post_iceauth_api_v2_users_json_password_resetrequest(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'Processed'
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json/password/resetRequest")
    api_info = obj_auth.post_iceauth_api_v2_users_json_password_resetrequest_helper(uid=name)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/json/password/resetRequest return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/json/password/resetRequest return payload:{api_info}"


def test_get_iceauth_api_v2_users_userroles(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'user'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users/userRoles")
    api_info = obj_auth.get_iceauth_api_v2_users_userroles_helper(uid=name)
    logger.info(f"TEST: test get call ICEAUTH/api/v2/users/userRoles return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert in api_info, f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"


def test_get_iceauth_api_v2_users_search(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = 'uid'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users/search")
    api_info = obj_auth.get_iceauth_api_v2_users_search_helper(uid=name)
    logger.info(f"TEST: test get call ICEAUTH/api/v2/users/search return payload: {api_info}")
    assert expected_assert in api_info[0], f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"


def test_post_iceauth_api_v2_users_lock(user, caplog):
    caplog.set_level(logger.INFO)
    name = user['username']
    expected_assert = "ACCOUNT_LOCKED"
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/lock")
    api_res = obj_auth.post_iceauth_api_v2_users_lock_helper(uid=name)
    logger.info(f"TEST: test post call ICEAUTH/api/v2/users/lock return payload: {api_res}")
    logger.info("TEST: test post  call: ICEAUTH/api/v2/users/json/password/update")
    api_info = obj_auth.post_iceauth_api_v2_users_json_password_update_helper(uid=name)
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ICEAUTH/api/v2/users/lock return payload:{api_info}"

