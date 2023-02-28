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
lookupDef = ["AGENCY", "QUERYTYPE", "QRYDATALEVEL", "PLOTOPTION", "COMPONENT", "COMPTYPE", "PERSISTENCE_DB",
             "PERSISTENCE_NON_DB","EXECUTION_STAGE","GRID_STAGE", "LANGUAGE"]


# @pytest.mark.parametrize("service_code_", service_code)
# @pytest.mark.parametrize("lookupDef_", lookupDef)
# @pytest.mark.parametrize("agency", agencies)
# def test_get_engine_rest_requestservice(service_code_, lookupDef_, agency, caplog):
#     caplog.set_level(logger.INFO)
#     expected_assert = 'displayValue'
#     logger.info("TEST: test get  call: ENGINE/rest/requestservice")
#     api_info = obj_auth.get_engine_rest_requestservice_helper(serviceCode=service_code_, lookupDefinitionId=lookupDef_,
#                                                               agencyId=agency, gatAgencyId=agency)
#     logger.debug(f"TEST: test get call ENGINE/rest/requestservice return payload: {api_info}")
#
#     assert expected_assert in api_info[0], f"test failed to assert positive"
#     f"Expected assert:{expected_assert} but actual does not exist"
# # import pdb
# #
# # pdb.set_trace()
