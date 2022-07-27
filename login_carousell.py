import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def login_carousell(driver, username, password):
    # Find the Sell Button
    search_btn = driver.find_element(
        By.XPATH, '//a[@href="/login"]')
    # Click on the Sell Button
    ActionChains(driver)\
        .click(search_btn)\
        .perform()

    # Wait until the Username Field Appears then fetch the element
    username = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//input[@type="text" and @name="username" and @aria-label="Username or email"]'))
    )
    # Enter the Username
    username.send_keys('tetanggakita')  # ! username or email

    time.sleep(3)

    # Find the Password Field
    password = driver.find_element(
        By.XPATH, '//input[@type="password" and @name="password" and @aria-label="Password"]')
    # Enter the Password
    password.send_keys('Ph1lodendron')  # ! password

    time.sleep(3)

    # Find the Login Button
    login_btn = driver.find_element(
        By.XPATH, '//*[@id="ReactModalPortal-LOGIN"]/div/div/div/div/form/button[@type="submit" and @role="submitButton"]')
    # Click on the Login Button
    ActionChains(driver)\
        .click(login_btn)\
        .perform()
