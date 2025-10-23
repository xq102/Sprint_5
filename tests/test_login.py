import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from helpers import register_user

class TestLogin:

    def test_login_via_main_page_button(self, driver):
        email, password = register_user(driver)
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(BASKET_BUTTON))
        basket_link = driver.find_element(*BASKET_BUTTON)
        assert basket_link.is_displayed()

    def test_login_via_profile_link(self, driver):
        email, password = register_user(driver)
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MAIN_PROFILE_LINK).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(BASKET_BUTTON))
        basket_link = driver.find_element(*BASKET_BUTTON)
        assert basket_link.is_displayed()

    def test_login_via_registration_form_link(self, driver):
        email, password = register_user(driver)
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_REG_LINK).click()
        driver.find_element(*REG_LOGIN_LINK).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(BASKET_BUTTON))
        basket_link = driver.find_element(*BASKET_BUTTON)
        assert basket_link.is_displayed()

    def test_login_via_forgot_password_link(self, driver):
        email, password = register_user(driver)
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
        driver.find_element(*LOGIN_RESTORE_LINK).click()
        driver.find_element(*REG_LOGIN_LINK).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(BASKET_BUTTON))
        basket_link = driver.find_element(*BASKET_BUTTON)
        assert basket_link.is_displayed()
        