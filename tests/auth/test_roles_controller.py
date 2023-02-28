import time

import pytest

from helpers.auth.RolesController import RolesController
from utilities.genericUtilities import *
from helpers.auth.UserControllerV2 import UserControllerV2

obj_roles = UserControllerV2()
obj_auth = RolesController()


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


def test_get_iceauth_api_roles_getallroles(caplog):
    logger.info("TEST: test get  call: ICEAUTH/api/roles/getAllRoles")
    api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId='6000003')
    logger.debug(f"TEST: test get call ICEAUTH/api/roles/getAllRoles return payload: {api_info}")
    assert len(api_info) > 0, f"test failed to assert positive"
    f"Expected list of roles:{api_info} is empty"


def test_post_iceauth_api_roles_addusertorole(role_agency_id, caplog):
    caplog.set_level(logger.INFO)
    role = role_agency_id['role']
    agency = role_agency_id['agency']
    logger.info("TEST:test post  call:ICEAUTH/api/roles/addUserToRole")
    api_info = obj_auth.post_iceauth_api_roles_addusertorole_helper(uid="lungilem", roleName=role, agencyId=agency)
    logger.debug(f"TEST:test post call ICEAUTH/api/roles/addUserToRole return payload:{api_info}")

    # import pdb
    #
    # pdb.set_trace()
    assert True


def test_delete_iceauth_api_roles_removeuserfromrole(user, role, caplog):
    caplog.set_level(logger.INFO)
    role = role
    agency = '0'
    name = user
    logger.info("TEST: test delete  call: ICEAUTH/api/roles/removeUserFromRole")
    api_info = obj_auth.delete_iceauth_api_roles_removeuserfromrole_helper(uid=name, roleName=role, agencyId=agency)
    logger.debug(f"TEST: test delete call ICEAUTH/api/roles/removeUserFromRole return payload: {api_info}")
    cond = find_users(user_name=name, agency=agency, role=role)

    assert cond == False, f"test failed to assert positive" \
                          f"Expected role: {role} still assigned to user: {name} in agency: {agency} in user dictionary"
