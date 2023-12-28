import inspect
import logging

import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setupURL")
class Baseclass:

    def getLogger(self):
        testName = inspect.stack()[1][3]  # to get the exact test case name
        logger = logging.getLogger(testName)  # return testcase name
        fileHandler = logging.FileHandler('logfile.log')

        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)

        logger.setLevel(logging.DEBUG)
        return logger


    def varifyLinkPresence(self,text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, text)))


    def varifyCheckboxPresence(self):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH, "//div[@class='checkbox checkbox-primary']")))

    def selectDropdown(self,locator,text):
        dropDown = Select(locator)
        dropDown.select_by_visible_text(text)

