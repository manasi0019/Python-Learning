from selenium.webdriver.common.by import By

from PyAuto.PyAutoHeal import class_attributes
from PyAuto.PyAutoSelenium import PyAutoWeb
from config import TestConfig as config


class SelEasyHomePage(PyAutoWeb):
    # Define all the locators here. Multiple locator strategy is used,
    # if any one locator fails, framework will take up next in the list
    locatorOthersDropdown = [(By.XPATH, '//a[text()="Others"]')]
    locatorDynamicDataLoadingOption = [(By.LINK_TEXT, "Dynamic Data Loading")]

    def __init__(self, driver, url=""):
        super().__init__(driver)  # call super class constructor
        if config.run_mode == 'capture' or config.run_mode == 'capture&heal':
            class_attributes(self)
        self.driver = driver
        # if you create an object with url, it will validate the url for current page
        self.url = driver.current_url if url == "" else url
        if driver.current_url != self.url:
            self.driver.get(self.url)

    # methods to perform operation in the page following page object model
    def click_others_dropdown(self):
        self.click_wait_locator(self.locatorOthersDropdown)
        return self

    def click_dynamic_data_loading(self):
        self.click_wait_locator(self.locatorDynamicDataLoadingOption)
        return self
