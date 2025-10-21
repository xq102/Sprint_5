from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from locators import *
from generators import generate_email, generate_password

def register_user(driver):
    driver.get("https://stellarburgers.education-services.ru/")
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

def login_user(driver):
    driver.get("https://stellarburgers.education-services.ru/")
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_LOGIN_BUTTON)
    )
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
    driver.find_element(*LOGIN_EMAIL_INPUT).send_keys(email)
    driver.find_element(*LOGIN_PASSWORD_INPUT).send_keys(password)
    driver.find_element(*LOGIN_SUBMIT_BUTTON).click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(MAIN_PROFILE_LINK)
    )
    