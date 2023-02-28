import pytest

from helpers.auth.TokenController import TokenController
from helpers.engine.CfgActivityRestController import CfgActivityRestController
from utilities.genericUtilities import *

obj_auth = CfgActivityRestController()
login_check = TokenController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
language = INT_HOST[os.environ.get('ENV', 'language')]
role_path = INT_HOST[os.environ.get('ENV', 'roles_path')]
service_code = ["FIND_ACTIVE_BY_LKUP_CODE_DEF"]
lookupDef = ["AGENCY", "COMPONENT", "COMPTYPE", "PERSISTENCE_DB", "PERSISTENCE_NON_DB", "QUERYTYPE", "QRYDATALEVEL"]

#
# def test_get_engine_rest_activity_loadlistactivitymetadata(caplog):
#     caplog.set_level(logger.INFO)
#     expected_assert = 'activityCd'
#     logger.info("TEST: test get  call: ENGINE/rest/activity/loadListActivityMetaData")
#     api_info = obj_auth.get_engine_rest_activity_loadlistactivitymetadata_helper(language="en", agencyId="9000008",
#                                                                                  activityCd='LMTests')
#     logger.debug(f"TEST: test get call ENGINE/rest/activity/loadListActivityMetaData return payload: {api_info}")
#     assert expected_assert in api_info, f"test failed to assert positive"
#     f"Expected assert:{expected_assert} but actual does not exist"
#
#
# @pytest.mark.parametrize("agency", agencies)
# def test_get_engine_rest_activity_findallforagencyid(agency, caplog):
#     expected_assert = 'cfgActivityId'
#     logger.info("TEST: test get  call: ENGINE/rest/activity/findAllForAgencyId")
#     api_info = obj_auth.get_engine_rest_activity_findallforagencyid_helper(agencyId=agency)
#     logger.debug(f"TEST: test get call ENGINE/rest/activity/findAllForAgencyId return payload: {api_info}")
#     f"TEST:test get call ENGINE/rest/activity/findAllForAgencyId return payload:{api_info}"
#     assert expected_assert in api_info[0], f"test failed to assert positive" \
#                                            f"Expected assert:{expected_assert} but actual does not exist"
#     # import pdb
    #
    # pdb.set_trace()
