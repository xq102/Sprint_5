# tests/test_login.py
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from generators import generate_email, generate_password

def register_user(driver):
    driver.get("https://stellarburgers.education-services.ru/  ")
    driver.find_element(*MAIN_LOGIN_BUTTON).click()
    driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

    email = generate_email()
    password = generate_password()

    driver.find_element(*REG_NAME_INPUT).send_keys("vera")
    driver.find_element(*REG_EMAIL_INPUT).send_keys(email)
    driver.find_element(*REG_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*REG_SUBMIT_BUTTON).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON))
    return email, password

class TestLogin:

    def test_login_via_main_page_button(self, driver):
        email, password = register_user(driver)
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_PROFILE_LINK))
        assert "Личный Кабинет" in driver.page_source

    def test_login_via_profile_link(self, driver):
        email, password = register_user(driver)
        driver.get("https://stellarburgers.education-services.ru/  ")
        driver.find_element(*MAIN_PROFILE_LINK).click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_PROFILE_LINK))
        assert "Личный Кабинет" in driver.page_source

    def test_login_via_registration_form_link(self, driver):
        email, password = register_user(driver)
        driver.get("https://stellarburgers.education-services.ru/  ")
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_PROFILE_LINK))
        assert "Личный Кабинет" in driver.page_source

    def test_login_via_forgot_password_link(self, driver):
        email, password = register_user(driver)
        driver.get("https://stellarburgers.education-services.ru/  ")
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()='Восстановить пароль']").click()
        driver.find_element(By.XPATH, "//a[text()='Войти']").click()
        driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
        driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*LOGIN_SUBMIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable(MAIN_PROFILE_LINK))
        assert "Личный Кабинет" in driver.page_source
