import pytest

from helpers.engine.CfgEntityAttributeRestController import CfgEntityAttributeRestController
from utilities.genericUtilities import *

obj_auth = CfgEntityAttributeRestController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]


@pytest.mark.parametrize("agency", agencies)
def test_get_engine_rest_cfgentityattribute_findbyentitytypecd(agency, caplog):
    expected_assert = 'cfgEntityAttributeId'
    logger.info("TEST: test get  call: ENGINE/rest/cfgentityattribute/findByEntityTypeCd")
    api_info = obj_auth.get_engine_rest_cfgentityattribute_findbyentitytypecd_helper(agencyId=agencies)
    logger.debug(f"TEST: test get call ENGINE/rest/cfgentityattribute/findByEntityTypeCd return payload: {api_info}")
    f"TEST:test get call ENGINE/rest/cfgentityattribute/findByEntityTypeCd return payload:{api_info}"
    assert expected_assert in api_info[0], f"test failed to assert positive"
    f"Expected assert:{expected_assert} but actual does not exist"
