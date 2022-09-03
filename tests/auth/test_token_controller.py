import logging as logger
import pytest

from helpers.auth_helpers import AuthHelper

auth_obj = AuthHelper()


def test_auth_login():
    logger.info("TEST: test that a user can login to AUTH")
    api_info = auth_obj.login_to_auth_helper()
    logger.debug(f"The payload of 'test_auth_login()' TCID01: {api_info}")
    assert api_info['token_type'] == 'bearer', f"test failed to retrieve a token {api_info}"


@pytest.mark.regression
def test_create_new_user():
    logger.info("TEST: test that a new user can be created on AUTH")
    api_info = auth_obj.create_new_user_helper()
    logger.debug(f"The payload of 'test_create_new_user()' TCID02: {api_info}")
    assert api_info['message'] == 'User created', f"test failed to create new user {api_info}"
