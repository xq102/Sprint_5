import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from locators import *
from generators import generate_email, generate_password

class TestRegistration:

    def test_successful_registration(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        email = generate_email()
        password = generate_password()

        driver.find_element(*REG_NAME_INPUT).send_keys("vera")
        driver.find_element(*REG_EMAIL_INPUT).send_keys(email)
        driver.find_element(*REG_PASSWORD_INPUT).send_keys(password)
        driver.find_element(*REG_SUBMIT_BUTTON).click()

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(LOGIN_SUBMIT_BUTTON)
        )
        assert "Войти" in driver.page_source

    def test_registration_with_short_password_shows_error(self, driver):
        driver.get("https://stellarburgers.education-services.ru/")
        driver.find_element(*MAIN_LOGIN_BUTTON).click()
        driver.find_element(By.XPATH, "//a[text()='Зарегистрироваться']").click()

        driver.find_element(*REG_NAME_INPUT).send_keys("vera")
        driver.find_element(*REG_EMAIL_INPUT).send_keys("vera@test.ru")
        driver.find_element(*REG_PASSWORD_INPUT).send_keys("123")
        driver.find_element(*REG_SUBMIT_BUTTON).click()

        error = driver.find_element(*REG_ERROR_MESSAGE)
        assert error.is_displayed()
        assert "Некорректный пароль" in error.text