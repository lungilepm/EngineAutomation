import pytest

from helpers.mlcs.LookupCodeRestController import LookupCodeRestController
from utilities.genericUtilities import *

obj_auth = LookupCodeRestController()

lookupDefinitionId = ['LKMODULE', 'AGENCY']
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]


@pytest.mark.parametrize("lookupDefinition", lookupDefinitionId)
@pytest.mark.parametrize("agency", agencies)
def test_get_mlcs_secure_lookupcodes_findallactivebylookupdefinitionid(agency,lookupDefinition, caplog):
    caplog.set_level(logger.INFO)
    expected_assert = 'lookupCode'
    logger.info("TEST:test get  call:MLCS/secure/lookupCodes/findAllActiveByLookupDefinitionId")
    api_info = obj_auth.get_mlcs_secure_lookupcodes_findallactivebylookupdefinitionid_helper(agencyId=agency,
                                                                                             lookupDefinitionId=lookupDefinition)
    logger.debug(
        f"TEST:test get call MLCS/secure/lookupCodes/findAllActiveByLookupDefinitionId return payload:{api_info}")
    assert expected_assert in api_info[0], f"test failed to assert positive" #Check if the api_info has lookupCode parameter
    f"Expected assert:{expected_assert} but actual does not exist"
