import os
import logging as logger

from selenium.webdriver.common.by import By

from configs.hosts_config import INT_HOST


class BOMHeaderPage(object):

    def __init__(self, driver):
        navbar_brand = "//a[@class='navbar-brand text-success']"
        entities_drop = "//*[text()='Processes ']"
        # username = "//*[@id='username']"
        # old_password = "//*[@id='oldPassword']"
        # new_password = "//*[@id='newPassword']"
        # confirm_password = "//*[@id='confirmPassword']"
        # cancel_submit = "//*[text()=' Cancel ']"
        titleText = ""
        self.driver = driver
        self.navbar_brand_ = driver.find_element(By.XPATH, navbar_brand)
        # self.username_ = driver.find_element(By.XPATH, username)
        # self.new_password_ = driver.find_element(By.XPATH, new_password)
        # self.old_password_ = driver.find_element(By.XPATH, old_password)
        # self.confirm_password_ = driver.find_element(By.XPATH, confirm_password)
        # self.cancel_submit_ = driver.find_element(By.XPATH, cancel_submit)

    def is_bom_brand_visible(self):
        well = self.navbar_brand_.is_displayed()
        logger.info(f"Click the BOMUI brand text")
        return well

    # def set_username(self, str_username=None):
    #     if not str_username:
    #         str_username = INT_HOST[os.environ.get('ENV', 'username')]
    #     self.username_.send_keys(str_username)
    #     logger.info(f"Enter test username: {str_username} into text field")
    #
    # def set_old_password(self, str_password):
    #     if not str_password:
    #         str_password = 'old_pass'
    #     self.old_password_.send_keys(str_password)
    #     logger.info(f"Enter test old password: {str_password} into text field")
    #
    # def set_new_password(self, str_password=None):
    #     if not str_password:
    #         str_password = 'new_pass'
    #     self.new_password_.send_keys(str_password)
    #     logger.info(f"Enter test NEW password: {str_password} into text field")
    #
    # def set_confirm_password(self, str_password=None):
    #     if not str_password:
    #         str_password = 'new_pass'
    #     self.confirm_password_.send_keys(str_password)
    #     logger.info(f"Enter CONFIRM password: {str_password} into text field")
    #
    # def click_cancel(self):
    #     self.cancel_submit_.click()
    #     logger.info(f"Login click to submit")
    #
    # def change_password(self, old_password=None, confirm_password=None,
    #                     new_password=None):
    #
    #     self.set_old_password(old_password)
    #     self.set_new_password(new_password)
    #     self.set_confirm_password(confirm_password)
    #     change_password = "//*[text()=' Change Password ']"
    #     self.driver.find_element(By.XPATH, change_password).click()
    #
    #     logger.info(f"Click on change password button")
    #     import pdb
    #
    #     pdb.set_trace()
