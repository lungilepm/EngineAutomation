import pytest

from helpers.auth.RolesController import RolesController
from helpers.auth.UserControllerTwo import UserControllerTwo
from utilities.genericUtilities import *

obj_auth = RolesController()
obj_roles = UserControllerTwo()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]
role_path = INT_HOST[os.environ.get('ENV', 'roles_path')]
pytest.fixture()


def role_list():
    values = read_doc(role_path, "json")
    # import pdb
    #
    # pdb.set_trace()
    for key in values:
        yield key


@pytest.mark.parametrize("user", role_list())
@pytest.mark.parametrize("role", baseRoles)
def test_post_iceauth_api_roles_addusertorole(user, role):
    name = user['username']
    agency = '0'
    print(f"therole:{user}:{role}")
    logger.info("TEST:test post  call:ICEAUTH/api/roles/addUserToRole")
    api_info = obj_auth.post_iceauth_api_roles_addusertorole_helper(uid=name, roleName=role, agencyId=user)
    logger.debug(f"TEST:test post call ICEAUTH/api/roles/addUserToRole return payload:{api_info}")
    user_role = obj_roles.get_iceauth_api_v2_users_helper(uid=name)
    actual_result = user_role[0]['authorities']
    expected_assert = user + "|" + role
    listing = {'authority': expected_assert}
    # import pdb
    #
    # pdb.set_trace()
    assert listing in actual_result, f"test failed to assert positive" \
                                     f"Expected assert: {listing} not in: {actual_result}"


@pytest.mark.parametrize("user", role_list())
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
