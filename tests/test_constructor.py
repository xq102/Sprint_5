import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *

class TestConstructor:
  
    def test_switch_to_sauces_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*CONSTRUCTOR_SAUCES_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CONSTRUCTOR_SAUCES_CURRENT)
        )
        assert driver.find_element(*CONSTRUCTOR_SAUCES_CURRENT)

    def test_switch_to_fillings_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*CONSTRUCTOR_FILLINGS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CONSTRUCTOR_FILLINGS_CURRENT)
        )  
        assert driver.find_element(*CONSTRUCTOR_FILLINGS_CURRENT)

    def test_switch_to_buns_section(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*CONSTRUCTOR_SAUCES_TAB).click()
        driver.find_element(*CONSTRUCTOR_BUNS_TAB).click()
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(CONSTRUCTOR_BUNS_CURRENT)
        )  
        assert driver.find_element(*CONSTRUCTOR_BUNS_CURRENT)
         