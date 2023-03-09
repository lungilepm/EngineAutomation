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
    # import pdb
    #
    # pdb.set_trace()
    bomObj = BOMHeaderPage(api_info)
    assert bomObj.is_bom_brand_visible()


def test_change_password(get_driver, caplog):
    driver = get_driver
    urls = base_url
    caplog.set_level(logger.INFO)
