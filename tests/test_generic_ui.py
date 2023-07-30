import pytest

from pages.bomui.BOMHeaderPage import BOMHeaderPage
from pages.genericui.LoginPage import LoginPage
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
    api_info = loginObj.login()
    # import pdb
    #
    # pdb.set_trace()
    bomObj = BOMHeaderPage(driver)
    bomObj. export_configuration()


# def test_change_password(get_driver, caplog):
#     driver = get_driver
#     urls = base_url
#     caplog.set_level(logger.INFO)
