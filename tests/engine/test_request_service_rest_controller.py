import pytest

from helpers.auth.TokenController import TokenController
from helpers.auth.UserControllerTwo import UserControllerTwo
from helpers.engine.CfgConditionRestController import CfgConditionRestController
from helpers.engine.RequestServiceRestController import RequestServiceRestController
from utilities.genericUtilities import *

obj_auth = RequestServiceRestController()
login_check = TokenController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]
role_path = INT_HOST[os.environ.get('ENV', 'roles_path')]

pytest.fixture()


def comp_id():
    values = ["FIND_ACTIVE_BY_LKUP_CODE_DEF"]
    # import pdb
    #
    # pdb.set_trace()
    for key in values:
        yield key

    print(f"After the test: {values}")


@pytest.mark.parametrize("comp", comp_id())
def test_get_engine_rest_requestservice(comp):
    expected_assert = 'displayValue'
    logger.info("TEST: test get  call: ENGINE/rest/requestservice")
    api_info = obj_auth.get_engine_rest_requestservice_helper()
    logger.debug(f"TEST: test get call ENGINE/rest/requestservice return payload: {api_info}")

    assert expected_assert in api_info[0], f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"
# import pdb
#
# pdb.set_trace()
