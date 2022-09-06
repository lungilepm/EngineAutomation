import logging as logger
import pytest
from helpers.auth_helpers import AuthHelper


obj_auth = AuthHelper()


def test_post_oauth_token():
    logger.info("TEST: test that a user can login to AUTH")
    api_info = obj_auth.post_oauth_token_helper()
    assert api_info['token_type'] == 'bearer', f"test failed to retrieve a token {api_info}"


@pytest.mark.regression
def test_api_v2_users_json():
    logger.info("TEST: test that a new user can be created on AUTH")
    api_info = obj_auth.post_api_v2_users_json_helper()
    assert api_info['message'] == 'User created', f"test failed to create new user {api_info}"
