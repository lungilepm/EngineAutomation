import time

import pytest

from helpers.auth.RolesController import RolesController
from utilities.genericUtilities import *
from helpers.auth.UserControllerV2 import UserControllerV2

obj_roles = UserControllerV2()
obj_auth = RolesController()


def test_get_iceauth_api_roles_getallroles(caplog):
    logger.info("TEST: test get  call: ICEAUTH/api/roles/getAllRoles")
    api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId='6000003')
    logger.debug(f"TEST: test get call ICEAUTH/api/roles/getAllRoles return payload: {api_info}")
    assert len(api_info) > 0, f"test failed to assert positive"
    f"Expected list of roles:{api_info} is empty"


def test_post_iceauth_api_roles_addusertorole(user, role, caplog):
    caplog.set_level(logger.INFO)
    userMessage = 201
    logger.info("TEST:test post  call:ICEAUTH/api/roles/addUserToRole")
    api_info = obj_auth.post_iceauth_api_roles_addusertorole_helper(uid=user['username'], roleName=role,
                                                                    agencyId=0)
    logger.debug(f"TEST:test post call ICEAUTH/api/roles/addUserToRole return payload:{api_info}")

    # import pdb
    #
    # pdb.set_trace()
    # assert api_info['statusCode'] == userMessage


def test_delete_iceauth_api_roles_removeuserfromrole(user, role, caplog):
    caplog.set_level(logger.INFO)
    userMessage = 201
    logger.info("TEST: test delete  call: ICEAUTH/api/roles/removeUserFromRole")
    api_info = obj_auth.delete_iceauth_api_roles_removeuserfromrole_helper(uid=user['username'], roleName=role,
                                                                           agencyId=0)
    logger.debug(f"TEST: test delete call ICEAUTH/api/roles/removeUserFromRole return payload: {api_info}")
    # assert api_info['statusCode'] == userMessage
