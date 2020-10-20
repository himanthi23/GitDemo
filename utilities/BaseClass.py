import inspect
import logging

import pytest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.usefixtures("setup")
class BaseClass:
    def verifyLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.LINK_TEXT, text)))

    def verifyLinkPresenceByCss(self, text):
        wait = WebDriverWait(self.driver, 30).until(

            EC.presence_of_element_located((By.CSS_SELECTOR, text)))

    def verifyAllLinkPresence(self, text):
        wait = WebDriverWait(self.driver, 30).until(
            EC.presence_of_all_elements_located((By.XPATH, text)))

    def verifyLinkClickable(self, text):
        wait = WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, text)))

    def selectOptionByText(self, locator, text):
        gender = Select(locator)
        gender.select_by_visible_text(text)

    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)

        fileHandler = logging.FileHandler('logfile.log')
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        fileHandler.setFormatter(formatter)

        logger.addHandler(fileHandler)  # file handler object
        logger.setLevel(logging.INFO)
        return logger
