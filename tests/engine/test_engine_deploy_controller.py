import pytest

from helpers.engine.EngineDeployController import EngineDeployController
from utilities.genericUtilities import *

obj_auth = EngineDeployController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]


# @pytest.mark.parametrize("agency", agencies)
# def test_get_engine_rest_importexport_generatecompleteexportfiles(agency, export_mlcs_fix, export_engine_fix):
#     expected_assert = 'Listed results'
#     logger.info("TEST: test get  call: ENGINE/rest/importExport/generateCompleteExportFiles")
#     api_info = obj_auth.get_engine_rest_importexport_generatecompleteexportfiles_helper(agencyId=agency,
#                                                                                         exportPOE=False,
#                                                                                         exportENGINE=export_engine_fix,
#                                                                                         exportAuth=True,
#                                                                                         exportMLCS=export_mlcs_fix,
#                                                                                         excludeAgencyParents=True,
#                                                                                         includeAgencyChildren=True)
#
#     logger.debug(f"TEST: test get call ENGINE/rest/importExport/generateCompleteExportFiles return payload: {api_info}")
# actual_result = api_info['message']
# assert expected_assert == actual_result, f"test failed to assert positive"
# f"Expected assert: {expected_assert} but actual: {actual_result}"
# f"TEST:test get call ENGINE/rest/importExport/generateCompleteExportFiles return payload:{api_info}")
# assert expected_assert in api_info[0], f"test failed to assert positive"
# f"Expected assert:{expected_assert} but actual does not exist"
