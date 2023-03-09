import os
import logging as logger
from time import sleep

from selenium.webdriver.common.by import By

from configs.hosts_config import INT_HOST


class LoginPage(object):

    def __init__(self, driver):
        username = "//*[@id='username']"
        password = "//*[@id='password']"
        login_submit = "//*[text()=' Login ']"
        titleText = ""
        self.driver = driver
        self.username_ = driver.find_element(By.XPATH, username)
        self.password_ = driver.find_element(By.XPATH, password)
        self.login_submit_ = driver.find_element(By.XPATH, login_submit)
        self.userName = []

    def set_username(self, str_username=None):
        logger.info(f"Enter test username: {str_username} into text field")
        if not str_username:
            str_username = INT_HOST[os.environ.get('ENV', 'username')]
        self.username_.send_keys(str_username)
        return self.driver

    def set_password(self, str_password=None):
        logger.info(f"Enter test password: {str_password} into text field")
        if not str_password:
            str_password = INT_HOST[os.environ.get('ENV', 'password')]
        self.password_.send_keys(str_password)
        return self.driver

    def click_login(self):
        logger.info(f"Login click to submit")
        if self.login_submit_.is_displayed():
            self.login_submit_.click()

        return self.driver

    def set_login_details(self, str_username=None, str_password=None):
        logger.info(f"Set the login details on text fields")
        self.set_username(str_username)
        # import pdb
        #
        # pdb.set_trace()
        self.set_password(str_password)
        return self.driver

    def login_to_app(self, str_username=None, str_password=None):
        logger.info(f"Click on login button")
        self.set_login_details(str_username, str_password)
        self.click_login()
        return self.driver
        # import pdb
        #
        # pdb.set_trace()

    def click_change_password(self, str_username=None, str_password=None):

        logger.info(f"Click on change password button")
        self.set_login_details(str_username, str_password)
        change_password = "//*[text()=' Change Password ']"
        change_password_submit_ = self.driver.find_element(By.XPATH, change_password)
        if change_password_submit_.is_displayed():
            change_password_submit_.click()

        return self.driver
