import pytest

from helpers.auth.TokenController import TokenController
from helpers.engine.CfgConditionRestController import CfgConditionRestController
from utilities.genericUtilities import *

obj_auth = CfgConditionRestController()
login_check = TokenController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]
role_path = INT_HOST[os.environ.get('ENV', 'roles_path')]

pytest.fixture()


def comp_id():
    values = ["b67b322c-4e3a-4a7e-8d48-f4e1f3cc8ae9"]
    # import pdb
    #
    # pdb.set_trace()
    for key in values:
        yield key


@pytest.mark.parametrize("comp", comp_id())
def test_get_engine_rest_condition_findbycomponentid(comp, caplog):
    caplog.set_level(logger.INFO)
    expected_assert = 'b67b322c-4e3a-4a7e-8d48-f4e1f3cc8ae9'
    logger.info("TEST: test get  call: ENGINE/rest/condition/findByComponentId")
    api_info = obj_auth.get_engine_rest_condition_findbycomponentid_helper(componentGUID=comp)
    logger.debug(f"TEST: test get call ENGINE/rest/condition/findByComponentId return payload: {api_info}")
    actual_result = api_info[0]['cfgComponentId']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call ENGINE/rest/condition/findByComponentId return payload:{api_info}"

# import pdb
#
# pdb.set_trace()
