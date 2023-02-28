from helpers.engine.CfgActivityEditRestController import CfgActivityEditRestController
from utilities.genericUtilities import *

obj_auth = CfgActivityEditRestController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]


# def test_get_engine_rest_activityedit(caplog):
#     expected_assert = 'cfgActivityEditId'
#     logger.info("TEST: test get  call: ENGINE/rest/activityEdit")
#     api_info = obj_auth.get_engine_rest_activityedit_helper()
#     logger.debug(f"TEST: test get call ENGINE/rest/activityEdit return payload: {api_info}")
#     assert expected_assert in api_info[0], f"test failed to assert positive"
#     f"Expected assert:{expected_assert} but actual does not exist"
