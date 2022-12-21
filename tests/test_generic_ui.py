import pytest

from helpers.bomui.BOMHeaderPage import BOMHeaderPage
from helpers.genericui.ChangePassowrdPage import ChangePasswordPage
from helpers.genericui.LoginPage import LoginPage
from utilities.genericUtilities import *

base_url = INT_HOST[os.environ.get('ENV', 'intzw')]


def test_login_page(get_driver, caplog):
    driver = get_driver
    urls = base_url
    caplog.set_level(logger.INFO)
    base = urls + "BOMUI/#!/login"
    driver.get(base)
    # import pdb
    #
    # pdb.set_trace()
    loginObj = LoginPage(driver)

    logger.info("Test login to page")
    api_info = loginObj.login_to_app()
    bomObj = BOMHeaderPage(api_info)
    assert bomObj.is_bom_brand_visible()

    # assert expected_assert in api_info[0], f"test failed to assert positive"
    # f"Expected assert:{expected_assert} but actual does not exist"


def test_change_password_page(caplog, get_driver, one_user):
    driver = get_driver
    urls = base_url
    caplog.set_level(logger.INFO)
    base = urls + "BOMUI/#!/login"
    driver.get(base)
    loginObj = LoginPage(driver)
    logger.info("Test login to page")
    api_info = loginObj.click_change_password( str_username=one_user['username'])
    pwdObj = ChangePasswordPage(api_info)
    test = pwdObj.change_password(old_password=one_user['password'])


    # logger.debug(f"TEST: test get call ENGINE/rest/activityEdit return payload: {api_info}")
    # assert expected_assert in api_info[0], f"test failed to assert positive"
    # f"Expected assert:{expected_assert} but actual does not exist"
