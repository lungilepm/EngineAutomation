from helpers.auth.UserControllerTwo import UserControllerTwo
from utilities.genericUtilities import *
obj_auth = UserControllerTwo()
agencies = ['0']
baseRoles = ['AuthAdmin', 'SysAdmin', 'AudAdmin', 'CfgImporter', 'CFGADMIN', 'LookupAdmin', 'CFGTEMPLATE', 'AppAdmin',
             'AuthUser', 'System']


def test_get_iceauth_api_v2_users():
    expected_assert = 'authorities'
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users")
    api_info = obj_auth.get_iceauth_api_v2_users_helper()
    logger.debug(f"TEST: test get call ICEAUTH/api/v2/users return payload: {api_info}")
    assert expected_assert in api_info[0], f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"
