from helpers.mlcs.CallOutRestControllerSec import CallOutRestControllerSec
from utilities.genericUtilities import *

obj_auth = CallOutRestControllerSec()

agencies = INT_HOST[os.environ.get('ENV', 'agencies')]


def test_get_mlcs_secure_calloutservice_gethierarchymap():
    expected_assert = 0
    logger.info("TEST: test get  call: MLCS/secure/callOutService/getHierarchyMap")
    api_info = obj_auth.get_mlcs_secure_calloutservice_gethierarchymap_helper()
    logger.debug(f"TEST: test get call MLCS/secure/callOutService/getHierarchyMap return payload: {api_info}")
    actual_result = api_info['agencyId']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
