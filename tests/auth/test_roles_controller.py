import pytest
from helpers.auth.RolesController import RolesController
from helpers.auth.UserControllerTwo import UserControllerTwo
from utilities.genericUtilities import *

obj_auth = RolesController()
obj_roles = UserControllerTwo()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]

pytest.fixture()


def delete_list():
    values = read_doc("resources\logRoles", "json")
    # import pdb
    #
    # pdb.set_trace()
    for key in values:
        yield key


@pytest.mark.parametrize("user", delete_list())
@pytest.mark.parametrize("role", baseRoles)
def test_post_iceauth_api_roles_addusertorole(user, role):
    name = user['name']
    agency = '0'
    print(f"therole:{user}:{role}")
    logger.info("TEST:test post  call:ICEAUTH/api/roles/addUserToRole")
    api_info = obj_auth.post_iceauth_api_roles_addusertorole_helper(uid=name, roleName=role, agencyId=agency)
    logger.debug(f"TEST:test post call ICEAUTH/api/roles/addUserToRole return payload:{api_info}")
    user_role = obj_roles.get_iceauth_api_v2_users_helper(uid=name)
    actual_result = user_role[0]['authorities']
    expected_assert = agency + "|" + role
    listing = {'authority': expected_assert}
    # import pdb
    #
    # pdb.set_trace()
    assert listing in actual_result, f"test failed to assert positive" \
                                     f"Expected assert: {listing} not in: {actual_result}"


def remove_list():
    values = read_doc("resources\logRoles", "json")
    # import pdb
    #
    # pdb.set_trace()
    for key in values:
        yield key


@pytest.mark.parametrize("user", remove_list())
@pytest.mark.parametrize("role", baseRoles)
def test_delete_iceauth_api_roles_removeuserfromrole(user, role):
    name = user['name']
    agency = '0'
    logger.info("TEST: test delete  call: ICEAUTH/api/roles/removeUserFromRole")
    api_info = obj_auth.delete_iceauth_api_roles_removeuserfromrole_helper(uid=name, roleName=role, agencyId=agency)
    logger.debug(f"TEST: test delete call ICEAUTH/api/roles/removeUserFromRole return payload: {api_info}")
    user_role = obj_roles.get_iceauth_api_v2_users_helper(uid=name)
    actual_result = user_role[0]['authorities']
    expected_assert = agency + "|" + role
    listing = {'authority': expected_assert}
    # import pdb
    #
    # pdb.set_trace()
    assert listing not in actual_result, f"test failed to assert positive" \
                                         f"Expected assert: {listing} not in: {actual_result}"

    # assert expected_assert == actual_result
#
# @pytest.mark.parametrize("user", delete_list())
# @pytest.mark.parametrize("role", baseRoles)
# def test_delete_iceauth_api_roles_json_removeuserfromrole(user, role):
#     name = user['name']
#     logger.info("TEST: test delete  call: ICEAUTH/api/roles/json/removeUserFromRole")
#     api_info = obj_auth.delete_iceauth_api_roles_json_removeuserfromrole_helper(uid=name, roleName=role, agencyId='0')
#     logger.debug(f"TEST: test delete call ICEAUTH/api/roles/json/removeUserFromRole return payload: {api_info}")
#     # actual_result = api_info['message']
#     # assert expected_assert == actual_result, f"test failed to assert positive"
#     # f"Expected assert: {expected_assert} but actual: {actual_result}"
#
#
# # @pytest.mark.parametrize("user", delete_list())
# # @pytest.mark.parametrize("role", baseRoles)
# # def test_post_iceauth_api_roles_json_addusertorole(user, role):
# #     expected_assert = 'Listed results'
# #     logger.info("TEST: test post  call: ICEAUTH/api/roles/json/addUserToRole")
# #     api_info = obj_auth.post_iceauth_api_roles_json_addusertorole_helper()
# #     logger.debug(f"TEST: test post call ICEAUTH/api/roles/json/addUserToRole return payload: {api_info}")
# #     actual_result = api_info['message']
# #     assert expected_assert == actual_result, f"test failed to assert positive"
# #     f"Expected assert: {expected_assert} but actual: {actual_result}"
#
#
# @pytest.mark.parametrize("agency", agencies)
# def test_get_iceauth_api_roles_getallroles(agency):
#     expected_assert = 'AuthAdmin'
#     logger.info("TEST: test get  call: ICEAUTH/api/roles/getAllRoles")
#     api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId=agency)
#     logger.debug(f"TEST: test get call ICEAUTH/api/roles/getAllRoles return payload: {api_info}")
#     actual_result = api_info['AuthAdmin']
#     assert expected_assert in actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"
#
#
# def test_get_iceauth_api_v2_users():
#     expected_assert = INT_HOST[os.environ.get('ENV', 'username')].lower()
#     logger.info("TEST: test get  call: ICEAUTH/api/v2/users")
#     api_info = obj_auth.get_iceauth_api_v2_users_helper()
#     logger.debug(f"TEST: test get call ICEAUTH/api/v2/users return payload: {api_info}")
#     actual_result = api_info[0]['username'].lower()
#     assert expected_assert == actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"
#
#
# def test_post_iceauth_api_roles_json_addusertorole():
#     expected_assert = 'Listed results'
#     logger.info("TEST: test post  call: ICEAUTH/api/roles/json/addUserToRole")
#     api_info = obj_auth.post_iceauth_api_roles_json_addusertorole_helper()
#     logger.debug(f"TEST: test post call ICEAUTH/api/roles/json/addUserToRole return payload: {api_info}")
#     actual_result = api_info['message']
#     assert expected_assert == actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"
