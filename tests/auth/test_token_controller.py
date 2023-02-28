from helpers.auth.TokenController import TokenController
from utilities.genericUtilities import *

obj_auth = TokenController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = ['AuthAdmin', 'SysAdmin', 'AudAdmin', 'CfgImporter', 'CFGADMIN', 'LookupAdmin', 'CFGTEMPLATE', 'AppAdmin',
             'AuthUser', 'System']


# def test_post_iceauth_oauth_token(caplog):
#     caplog.set_level(logger.INFO)
#     expected_assert = 'bearer'
#     logger.info("TEST: test post  call: ICEAUTH/oauth/token")
#     api_info = obj_auth.post_iceauth_oauth_token_helper()
#     logger.debug(f"TEST: test post call ICEAUTH/oauth/token return payload: {api_info}")
#     actual_result = api_info['token_type']
#     assert expected_assert == actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"
