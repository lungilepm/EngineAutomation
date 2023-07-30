import logging as logger
from time import sleep

import os

from selenium.webdriver.common.by import By

from configs.hosts_config import INT_HOST
from pages.BasePage import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.username = (By.XPATH, "//*[@id='username']")
        self.password = (By.XPATH, "//*[@id='password']")
        self.login_submit = (By.XPATH, "//*[text()=' Login ']")
        self.base_url = INT_HOST[os.environ.get('ENV', 'intzw')]

    def login(self, username=None, password=None):
        self.wait_for(self.login_submit)
        if not username:
            username = INT_HOST[os.environ.get('ENV', 'username')]
        self.send_keys(self.username, username)
        if not password:
            password = INT_HOST[os.environ.get('ENV', 'password')]
        self.send_keys(self.password, password)
        self.click(self.login_submit)
