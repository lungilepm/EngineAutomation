import pytest

from helpers.engine.CFGQueryRestController import CfgQueryRestController
from utilities.genericUtilities import *

obj_auth = CfgQueryRestController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]


@pytest.mark.parametrize("agency", agencies)
def test_get_engine_rest_cfgquery_findallforagencyid(agency, caplog):
    expected_assert = 'cfgQueryId'
    logger.info("TEST: test get  call: ENGINE/rest/cfgQuery/findAllForAgencyId")
    api_info = obj_auth.get_engine_rest_cfgquery_findallforagencyid_helper(agencyId=agency)
    logger.debug(f"TEST: test get call ENGINE/rest/cfgQuery/findAllForAgencyId return payload: {api_info}")
    f"TEST:test get call ENGINE/rest/cfgQuery/findAllForAgencyId return payload:{api_info}"
    assert expected_assert in api_info[0], f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"
