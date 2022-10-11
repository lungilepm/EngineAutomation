from helpers.auth.TokenControllerTwo import TokenControllerTwo
from utilities.genericUtilities import *

obj_auth = TokenControllerTwo()
agencies = ['0']
baseRoles = ['AuthAdmin', 'SysAdmin', 'AudAdmin', 'CfgImporter', 'CFGADMIN', 'LookupAdmin', 'CFGTEMPLATE', 'AppAdmin',
             'AuthUser', 'System']


def test_post_iceauth_api_v2_users_json():
    expected_assert = 'User created'
    logger.info("TEST: test post  call: iceauth/api/v2/users/json")
    api_info = obj_auth.post_iceauth_api_v2_users_json_helper()
    logger.debug(f"TEST: test that a post can access iceauth/api/v2/users/json return payload {api_info}")
    actual_result = api_info['message']
    assert expected_assert == actual_result, f"test failed to assert positive"
    f"Expected assert: {expected_assert} but actual: {actual_result}"
#
#
# def test_get_iceauth_api_v2_users_json():
#     expected_assert = 'Listed results'
#     logger.info("TEST: test that a get can access iceauth/api/v2/users/json")
#     api_info = obj_auth.get_iceauth_api_v2_users_json_helper()
#     logger.debug(f"TEST: test that a get can access iceauth/api/v2/users/json return payload {api_info}")
#     actual_result = api_info['message']
#     assert expected_assert == actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"
#
#
# def test_get_iceauth_api_realms():
#     expected_assert = INT_HOST[os.environ.get('ENV', 'realm')]
#     logger.info("TEST: test that a get can access iceauth/api/realms")
#     api_info = obj_auth.get_iceauth_api_realms_helper()
#     logger.debug(f"TEST: test that a get can access iceauth/api/realms return payload {api_info}")
#     actual_result = api_info[0]['name']
#     assert expected_assert == actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"

# pytest.fixture()
# 
#
# @pytest.mark.parametrize("agencyid", agencies)
# def get_iceauth_api_roles_getallroles(agencyid):
#     logger.info("TEST: test get  call: iceauth/api/roles/getallroles")
#     api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId=agencyid)
#     values = api_info.values()
#     logger.debug(f"TEST: test get call iceauth/api/roles/getallroles return payload: {api_info}")
#     roles_per_agent = list(values)
#     logger.debug(f"Roles:  {roles_per_agent}")
#     for x in roles_per_agent:
#         yield x
#
#
# @pytest.mark.order1
# @pytest.mark.parametrize("role_name", get_iceauth_api_roles_getallroles(agencies))
# def test_post_iceauth_api_roles_addusertorole(role_name):
#     create_user = obj_auth.post_iceauth_api_v2_users_json_helper()
#     uid = create_user['data'][0]['uid']
#     password = create_user['data'][0]['userPassword']
#     agencyId = agencies[0]
#     # import pdb
#     # pdb.set_trace()
#     strName = f"\"{uid}\", \"{password}\", \"{role_name}\"\n"
#     write_to_text(file_path="resources\logRoles", to_write=strName, file_type="csv", mode="a")
#     logger.info("TEST: test post  call: ICEAUTH/api/roles/addUserToRole")
#     api_info = obj_auth.post_iceauth_api_roles_addusertorole_helper(uid=uid, roleName=role_name, clearCache=True,
#                                                                     agencyId=agencyId)
#     logger.debug(f"TEST: test post call ICEAUTH/api/roles/addUserToRole return payload: {api_info}")


# pytest.fixture()
#
#
# def delete_list():
#     values = read_doc("resources\logRoles", "csv", "tuple")
#     for row in values:
#         yield row

#
# @pytest.mark.parametrize("name, password, role", delete_list())
# def test_delete_iceauth_api_v2_users_json(name, password, role):
#     name = name.strip()
#     password = password.strip()
#     role = role.strip()
#     print(f"name:{name}, pass:{password}, role:{role}")
#     expected_assert = 'User deleted'
#     logger.info("TEST: test delete  call: ICEAUTH/api/v2/users/json")
#     api_user = obj_auth.post_iceauth_oauth_token_helper(username=name, password=password)
#
#     api_del = obj_auth.delete_iceauth_api_v2_users_json_helper(uid=name)
#
#     logger.debug(f"TEST: test delete call ICEAUTH/api/v2/users/json return payload: {api_user}")
#     actual_result = api_user['message']
#     assert expected_assert == actual_result, f"test failed to assert positive"
#     f"Expected assert: {expected_assert} but actual: {actual_result}"
#     write_to_text("resources\deleted_list", name + "\n", "txt", "a")
