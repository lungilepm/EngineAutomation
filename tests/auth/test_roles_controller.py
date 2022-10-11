import pytest
from helpers.auth.TokenController import TokenController
from utilities.genericUtilities import *
from helpers.auth.RolesController import RolesController
from helpers.auth.TokenControllerTwo import TokenControllerTwo
from utilities.genericUtilities import *

obj_auth = RolesController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]

pytest.fixture()


def delete_list():
    values = read_doc("resources\logRoles", "json")

    for key in values:
        yield key


@pytest.mark.parametrize("role", baseRoles)
def test_post_iceauth_api_roles_addusertorole(role):
    logger.info("TEST:test post  call:ICEAUTH/api/roles/addUserToRole")
    api_info = obj_auth.post_iceauth_api_roles_addusertorole_helper(uid='lungile', roleName=role, agencyId='0')
    logger.debug(f"TEST:test post call ICEAUTH/api/roles/addUserToRole return payload:{api_info}")


@pytest.mark.parametrize("agency", agencies)
def test_get_iceauth_api_roles_getallroles(agency):
    expected_assert = 'AuthAdmin'
    logger.info("TEST: test get  call: ICEAUTH/api/roles/getAllRoles")
    api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId=agency)
    logger.debug(f"TEST: test get call ICEAUTH/api/roles/getAllRoles return payload: {api_info}")
    actual_result = api_info['AuthAdmin']
    assert expected_assert in actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_get_iceauth_api_v2_users():
    expected_assert = INT_HOST[os.environ.get('ENV', 'username')].lower()
    logger.info("TEST: test get  call: ICEAUTH/api/v2/users")
    api_info = obj_auth.get_iceauth_api_v2_users_helper()
    logger.debug(f"TEST: test get call ICEAUTH/api/v2/users return payload: {api_info}")
    actual_result = api_info[0]['username'].lower()
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"


def test_post_iceauth_api_roles_json_addusertorole():
    expected_assert = 'Listed results'
    logger.info("TEST: test post  call: ICEAUTH/api/roles/json/addUserToRole")
    api_info = obj_auth.post_iceauth_api_roles_json_addusertorole_helper()
    logger.debug(f"TEST: test post call ICEAUTH/api/roles/json/addUserToRole return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
