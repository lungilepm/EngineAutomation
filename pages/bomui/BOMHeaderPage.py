import os
from time import sleep

from selenium.webdriver.common.by import By
from seleniumpagefactory.Pagefactory import PageFactory
from configs.hosts_config import INT_HOST
from pages.BasePage import BasePage
from pages.bomui.HomePage import HomePage


class BOMHeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.base_url = INT_HOST[os.environ.get('ENV', 'intzw')]
        self.businessObjectManager_drop = (By.XPATH, '// *[text() = "Business Object Manager"]')
        self.entities_drop = (By.XPATH, '// *[text() = "Entities "]')
        self.processes_drop = (By.XPATH, '// *[text() = "Processes "]')
        self.templates_drop = (By.XPATH, '// *[text() = "Templates "]')
        self.export_Configuration = (By.XPATH, '// *[text() = "Import/Export Configuration"]')
        self.select_import = (By.XPATH, '//*[@id = "selectedOption"][1]')
        self.select_export = (By.XPATH, '//*[@id = "selectedOption"][2]')

    def processes_click(self):
        self.wait_for(self.processes_drop)
        sleep(3)
        self.click(self.processes_drop)
        sleep(3)
        self.click(self.export_Configuration)

    def import_configuration(self):
        self.processes_click()
        self.wait_for(self.select_import)

    def export_configuration(self):
        self.processes_click()
        self.wait_for(self.select_export)
