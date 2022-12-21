import time

import pytest

from helpers.auth.RolesController import RolesController
from utilities.genericUtilities import *
from helpers.auth.UserControllerV2 import UserControllerV2

obj_roles = UserControllerV2()
obj_auth = RolesController()
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
baseRoles = INT_HOST[os.environ.get('ENV', 'baseRoles')]


def find_users(user_name=None, agency=None, role=None):
    user_role = obj_roles.get_iceauth_api_v2_users_helper(uid=user_name)
    dict_of = user_role[0]['authorities']
    ind_num = find_role(dict_of)
    logger.info(f"\n Number of Roles user Has: {ind_num} ")
    for i, elem in enumerate(ind_num):
        role_in = user_role[0]['authorities'][i]['authority']
        role_split = role_in.split('|')
        test_agency = role_split[0]
        role_test = role_split[1].lower()
        if test_agency == agency and role_test == role.lower():
            return True
    return False


@pytest.mark.parametrize("agency", agencies)
def test_get_iceauth_api_roles_getallroles(agency, caplog):
    logger.info("TEST: test get  call: ICEAUTH/api/roles/getAllRoles")
    api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId=agency)
    logger.debug(f"TEST: test get call ICEAUTH/api/roles/getAllRoles return payload: {api_info}")
    assert len(api_info) > 0, f"test failed to assert positive"
    f"Expected list of roles:{api_info} is empty"


# @pytest.mark.parametrize("agency", agencies)
def test_post_iceauth_api_roles_addusertorole(one_user, role_agency, caplog):
    caplog.set_level(logger.INFO)
    role = role_agency['role']
    agency = role_agency['agency']
    name = one_user['username']
    logger.info("TEST:test post  call:ICEAUTH/api/roles/addUserToRole")
    api_info = obj_auth.post_iceauth_api_roles_addusertorole_helper(uid=name, roleName=role, agencyId=agency)
    logger.debug(f"TEST:test post call ICEAUTH/api/roles/addUserToRole return payload:{api_info}")
    cond = find_users(user_name=name, agency=agency, role=role)
    # import pdb
    #
    # pdb.set_trace()
    assert cond == True, f"test failed to assert positive" \
                         f"Expected role: {role} not assigned to user: {name} in agency: {agency} not in user dictionary"


@pytest.mark.parametrize("agency", agencies)
def test_post__iceauth_api_roles_json_addusertoroles(one_user, agency, caplog):
    caplog.set_level(logger.INFO)
    expected_assert = 'Added to role'
    logger.info("TEST: test post  call: /ICEAUTH/api/roles/json/addUserToRoles")
    api_info = obj_auth.post__iceauth_api_roles_json_addusertoroles_helper(uid=one_user['username'], agencyId=agency)
    logger.debug(f"TEST: test post call /ICEAUTH/api/roles/json/addUserToRoles return payload: {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
    f"TEST:test get call /ICEAUTH/api/roles/json/addUserToRoles return payload:{api_info}"


def test_delete_iceauth_api_roles_removeuserfromrole(one_user, role_agency, caplog):
    caplog.set_level(logger.INFO)
    role = role_agency['role']
    agency = role_agency['agency']
    name = one_user['username']
    logger.info("TEST: test delete  call: ICEAUTH/api/roles/removeUserFromRole")
    api_info = obj_auth.delete_iceauth_api_roles_removeuserfromrole_helper(uid=name, roleName=role, agencyId=agency)
    logger.debug(f"TEST: test delete call ICEAUTH/api/roles/removeUserFromRole return payload: {api_info}")
    cond = find_users(user_name=name, agency=agency, role=role)

    assert cond == False, f"test failed to assert positive" \
                          f"Expected role: {role} still assigned to user: {name} in agency: {agency} in user dictionary"
