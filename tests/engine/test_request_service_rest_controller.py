import pytest

from helpers.auth.TokenController import TokenController
from helpers.engine.RequestServiceRestController import RequestServiceRestController
from utilities.genericUtilities import *

obj_auth = RequestServiceRestController()
login_check = TokenController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]
role_path = INT_HOST[os.environ.get('ENV', 'roles_path')]
service_code = ["FIND_ACTIVE_BY_LKUP_CODE_DEF"]
lookupDef = ["AGENCY"]


@pytest.mark.parametrize("service_code", service_code)
@pytest.mark.parametrize("lookupDef", lookupDef)
@pytest.mark.parametrize("service_code", service_code)
@pytest.mark.parametrize("lookupDef", lookupDef)
def test_get_engine_rest_requestservice(service_code, lookupDef):
    expected_assert = 'displayValue'
    logger.info("TEST: test get  call: ENGINE/rest/requestservice")
    api_info = obj_auth.get_engine_rest_requestservice_helper()
    logger.debug(f"TEST: test get call ENGINE/rest/requestservice return payload: {api_info}")

    assert expected_assert in api_info[0], f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"
# import pdb
#
# pdb.set_trace()
