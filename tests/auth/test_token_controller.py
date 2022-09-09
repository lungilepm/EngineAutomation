import logging as logger
import os

import pytest

from configs.hosts_config import INT_HOST
from helpers.auth_helpers import AuthHelper

obj_auth = AuthHelper()


# pytest --html=reports/report.html

def test_post_iceauth_oauth_token():
    expected_assert = 'bearer'
    logger.info("TEST: test post call iceauth/oauth/token")
    api_info = obj_auth.post_iceauth_oauth_token_helper()
    logger.debug(f"TEST: test that a post can access iceauth/oauth/token return payload {api_info}")
    actual_result = api_info['token_type']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_post_iceauth_api_v2_users_json():
    expected_assert = 'User created'
    logger.info("TEST: test post  call: iceauth/api/v2/users/json")
    api_info = obj_auth.post_iceauth_api_v2_users_json_helper()
    logger.debug(f"TEST: test that a post can access iceauth/api/v2/users/json return payload {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_get_iceauth_api_v2_users_json():
    expected_assert = 'Listed results'
    logger.info("TEST: test that a get can access iceauth/api/v2/users/json")
    api_info = obj_auth.get_iceauth_api_v2_users_json_helper()
    logger.debug(f"TEST: test that a get can access iceauth/api/v2/users/json return payload {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_get_iceauth_api_realms():
    expected_assert = INT_HOST[os.environ.get('ENV', 'realm')]
    logger.info("TEST: test that a get can access iceauth/api/realms")
    api_info = obj_auth.get_iceauth_api_realms_helper()
    logger.debug(f"TEST: test that a get can access iceauth/api/realms return payload {api_info}")
    actual_result = api_info[0]['name']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
