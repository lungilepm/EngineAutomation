import os
import logging as logger
from time import sleep

from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By

from configs.hosts_config import INT_HOST


class ChangePasswordPage(object):

    def __init__(self, driver):
        username = "//*[@id='username']"
        old_password = "//*[@id='oldPassword']"
        new_password = "//*[@id='newPassword']"
        confirm_password = "//*[@id='confirmPassword']"
        cancel_submit = "//*[text()=' Cancel ']"
        titleText = ""
        self.driver = driver
        self.username_ = driver.find_element(By.XPATH, username)
        self.new_password_ = driver.find_element(By.XPATH, new_password)
        self.old_password_ = driver.find_element(By.XPATH, old_password)
        self.confirm_password_ = driver.find_element(By.XPATH, confirm_password)
        self.cancel_submit_ = driver.find_element(By.XPATH, cancel_submit)

    def set_username(self, str_username=None):
        if not str_username:
            str_username = INT_HOST[os.environ.get('ENV', 'username')]
        self.username_.send_keys(str_username)
        logger.info(f"Enter test username: {str_username} into text field")
        return self.driver

    def set_old_password(self, str_password):
        if not str_password:
            str_password = 'old_pass'
        self.old_password_.send_keys(str_password)
        logger.info(f"Enter test old password: {str_password} into text field")
        return self.driver

    def set_new_password(self, str_password=None):
        if not str_password:
            str_password = 'new_pass'
        self.new_password_.send_keys(str_password)
        logger.info(f"Enter test NEW password: {str_password} into text field")
        return self.driver

    def set_confirm_password(self, str_password=None):
        if not str_password:
            str_password = 'new_pass'
        self.confirm_password_.send_keys(str_password)
        logger.info(f"Enter CONFIRM password: {str_password} into text field")
        return self.driver

    def click_cancel(self):
        self.cancel_submit_.click()
        logger.info(f"Login click to submit")
        return self.driver

    def change_password(self, old_password=None, confirm_password=None,
                        new_password=None):

        self.set_old_password(old_password)
        self.set_new_password(new_password)
        self.set_confirm_password(confirm_password)

        change_password = "//*[text()=' Change Password ']"
        element = self.driver.find_element(By.XPATH, change_password)
        webdriver.ActionChains(self.driver).move_to_element(element).perform()
        element.click()
        logger.info(f"Click on change password button")
        return self.driver
        # import pdb
        #
        # pdb.set_trace()
