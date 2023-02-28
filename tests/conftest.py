from helpers.auth.TokenController import TokenController
from helpers.genericui.LoginPage import LoginPage
import pytest
from helpers.auth.RolesController import RolesController
from helpers.auth.UserController import UserController
from helpers.auth.UserControllerV2 import UserControllerV2
from utilities.genericUtilities import *
from webdriver_manager.chrome import ChromeDriverManager

from selenium import webdriver

obj_auth = RolesController()
obj_roles = UserController()
obj_roles2 = UserControllerV2()
login_check = TokenController()
base_url = INT_HOST[os.environ.get('ENV', 'intzw')]
agencies = INT_HOST[os.environ.get('ENV', 'agencies')]
export_poe = INT_HOST[os.environ.get('ENV', "exportPOE")]
export_auth = INT_HOST[os.environ.get('ENV', "exportAuth")]
exclude_agency_parents = INT_HOST[os.environ.get('ENV', "excludeAgencyParents")]
include_agency_children = INT_HOST[os.environ.get('ENV', "includeAgencyChildren")]
export_mlcs = INT_HOST[os.environ.get('ENV', "exportMLCS")]
export_engine = INT_HOST[os.environ.get('ENV', "exportENGINE")]
unallocated = INT_HOST[os.environ.get('ENV', "unallocated")]
include_children = INT_HOST[os.environ.get('ENV', "includeChildren")]
force = INT_HOST[os.environ.get('ENV', "force")]
add_roles = INT_HOST[os.environ.get('ENV', "baseRoles")]


def create_user():
    written = []
    logger.info("TEST: test get  call: ICEAUTH/api/users/getUsersForAgency/0")
    api_info = obj_roles.get_iceauth_api_users_getusersforagency_helper()
    logger.debug(f"TEST: test get call ICEAUTH/api/users/getUsersForAgency/0 return payload: {api_info[0]}")
    ind_num = find_index(api_info, 'LP', element='initials')
    logger.info(f"\n Number of users: {ind_num} ")

    for i, elem in enumerate(ind_num):
        print(f"the way: {written}")
        use = api_info[elem]['uid']
        dict_temp = {'username': use, 'password': api_info[elem]['userPassword']}
        written.append(dict_temp)
    # Load more

    api_info = obj_roles2.get_iceauth_api_v2_users_json_getusersforagency_helper(agencyId='0')
    logger.info(f"\n All user for the test case:\n{api_info}")
    ind_num = find_index(api_info['data'][0], 'LP', element='initials')
    for i, elem in enumerate(ind_num):

        use = api_info['data'][0][elem]['uid']
        passw = api_info['data'][0][elem]['userPassword']
        if use in api_info['data'][0]:
            dict_temp = {'username': use, 'password': passw}
            written.append(dict_temp)

    logger.info(f"User info: {written}")
    for j, key in enumerate(written):
        yield key


def create_role_agency_id():
    logger.info("TEST: test get  call: ICEAUTH/api/roles/getAllRoles")
    for i, agency in enumerate(agencies):
        api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId=agency)
        for key in api_info:
            yield {'role': key, 'agency': agency}


@pytest.fixture(params=create_user())
def user(request, caplog):
    # import pdb
    #
    # pdb.set_trace()
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=add_roles)
def role(request, caplog):
    # import pdb
    #
    # pdb.set_trace()
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=create_role_agency_id())
def role_agency_id(request, caplog):
    # import pdb
    #
    # pdb.set_trace()
    caplog.set_level(logger.INFO)
    yield request.param


def create_base():
    for i, tem in enumerate(agencies):
        agency = tem
        api_info = obj_auth.get_iceauth_api_roles_getallroles_helper(agencyId=agency)
        for j, key in enumerate(api_info):
            temp = {'agency': agency, 'role': key}
            # import pdb
            #
            # pdb.set_trace()
            yield temp


@pytest.fixture(params=export_poe)
def export_poe_fix(request, caplog):
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=export_auth)
def export_auth_fix(request, caplog):
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=exclude_agency_parents)
def exclude_agency_parents_fix(request, caplog):
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=include_agency_children)
def include_agency_children_fix(request, caplog):
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=export_mlcs)
def export_mlcs_fix(request, caplog):
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=export_engine)
def export_engine_fix(request, caplog):
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture(params=create_base())
def role_agency(request, caplog):
    caplog.set_level(logger.INFO)
    yield request.param


@pytest.fixture()
def get_driver(caplog):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


@pytest.fixture()
def driver_login(get_driver, caplog):
    drive = request.param
    drive.get(base_url + "BOMUI/#!/login")
    loginObj = LoginPage(drive)
    api_info = loginObj.login_to_app()
    logger.info("login to the application")
    yield api_info
