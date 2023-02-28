from helpers.auth.TokenControllerTwo import TokenControllerTwo
from utilities.genericUtilities import *

obj_auth = TokenControllerTwo()
agencies = ['0']
baseRoles = ['AuthAdmin', 'SysAdmin', 'AudAdmin', 'CfgImporter', 'CFGADMIN', 'LookupAdmin', 'CFGTEMPLATE', 'AppAdmin',
             'AuthUser', 'System']

#
# def test_post_iceauth_api_v2_users_json(caplog):
#     caplog.set_level(logger.INFO)
#     expected_assert = 'User created'
#     logger.info("TEST: test post  call: iceauth/api/v2/users/json")
#     api_info = obj_auth.post_iceauth_api_v2_users_json_helper()
#     logger.debug(f"TEST: test that a post can access iceauth/api/v2/users/json return payload {api_info}")
#     actual_result = api_info['message']
#     assert expected_assert == actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"

