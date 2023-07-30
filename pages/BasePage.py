from time import sleep

from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging as logger


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 20

    def handle_element(self, by_locator):

        try:
            element_present = EC.presence_of_element_located(by_locator)
            elem = WebDriverWait(self.driver, self.timeout).until(element_present)
            logger.debug(f"presence of element found by {by_locator}  continue execution ")
            return elem
        except TimeoutException:
            elem = self.driver.find_element(by_locator)
            logger.debug(f"Timed out failed to locate by {by_locator} script error ")
            return elem

    def handle_click(self, by_locator):

        try:
            element_present = EC.element_to_be_clickable(by_locator)
            elem = WebDriverWait(self.driver, self.timeout).until(element_present)
            logger.debug(f"presence of element found by {by_locator}  continue execution ")
            sleep(2)
            return elem
        except TimeoutException:
            elem = self.driver.find_element(by_locator)
            logger.debug(f"Timed out failed to locate by {by_locator} script error ")
            return elem

    def click(self, by_locator):
        # get element
        element = self.handle_element(by_locator)
        # create action chain object
        action = ActionChains(self.driver)
        # click the item
        action.click(on_element=element)
        # perform the operation
        action.perform()

    def send_keys(self, by_locator, value):
        self.handle_element(by_locator).send_keys(value)
        logger.debug(f"Entered test by {by_locator}: {value} into text field")

    def get_text(self, by_locator):
        return self.handle_element(by_locator).get_attribute("innerText")

    def wait_for(self, by_locator):
        self.handle_element(by_locator)

    def select_by_text(self, by_locator, option):
        select = Select(self.handle_element(by_locator))
        select.select_by_visible_text(option)
