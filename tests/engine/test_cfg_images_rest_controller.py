from helpers.engine.CfgImagesRestController import CfgImagesRestController
from utilities.genericUtilities import *

obj_auth = CfgImagesRestController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]


# def test_get_engine_rest_cfgimages(caplog):
#     expected_assert = 'cfgImagesId'
#     logger.info("TEST: test get  call: ENGINE/rest/cfgimages")
#     api_info = obj_auth.get_engine_rest_cfgimages_helper()
#     logger.debug(f"TEST: test get call ENGINE/rest/cfgimages return payload: {api_info}")
#     f"TEST:test get call ENGINE/rest/cfgimages return payload:{api_info}"
#     assert expected_assert in api_info[0], f"test failed to assert positive"
#     f"Expected assert:{expected_assert} but actual does not exist"
