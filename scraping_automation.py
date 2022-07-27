import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def scraping_automation(title, price, seller):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.carousell.sg/')

    # Find the Sell Button
    search_btn = driver.find_element(
        By.XPATH, '//a[@href="/sell/"]')
    # Click on the Sell Button
    ActionChains(driver)\
        .click(search_btn)\
        .perform()

    # Find the upload file button
    for i in range(1, 4):
        # Wait until the page is loaded then fetch the element
        upload_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@accept="image/png, image/jpeg" and @type="file"]'))
        )
        # insert / upload files
        upload_btn.send_keys(
            'C:/Users/62851/Desktop/Projects/imagebot/images/255766_' + str(i) + '.jpg')  # ! Images

    # Find the Category Selection
    category_select = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div')
    # Click on category selection to dropdown menu
    ActionChains(driver)\
        .click(category_select)\
        .perform()

    # Find the Category Search Bar
    category_search = driver.find_element(
        By.XPATH, '//input[@type="text" and @placeholder="Search for a category..."]')
    # Enter the category
    category_search.send_keys('Plants & Seeds')

    # Find the Plants & Seeds Menu
    plants_menu = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]')
    # Click on category selection to dropdown menu
    ActionChains(driver)\
        .click(plants_menu)\
        .perform()

    # Wait until the Listing Title Bar Appears then fetch the element
    listing_title = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//input[@type="text" and @name="field_title" and @placeholder="Name your listing"]'))
    )
    # Enter the Listing Title
    listing_title.send_keys(title)  # ! Title

    # Find the New Conditional Checkbox
    plants_menu = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[2]/div/div/div[1]')
    # Click on New Conditional Checkbox
    ActionChains(driver)\
        .click(plants_menu)\
        .perform()

    # Find the Price Bar
    listing_price = driver.find_element(
        By.XPATH, '//input[@type="number" and @name="field_price" and @placeholder="Price of your listing"]')
    # Enter the Price
    listing_price.send_keys(price)  # ! Price

    # Find the Description Bar
    listing_desc = driver.find_element(
        By.XPATH, '//textarea[@name="field_description"]')
    # Enter the Description
    listing_desc.send_keys(
        'Indoor plant\nEasy maintenance\n\nPlease chat to check its availability.\nThank you and happy shopping!\n\n' + seller)  # ! Description

    # Find the Delevery Cehckbox
    delevery_cehckbox = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/label')
    # Click on Delevery Cehckbox
    ActionChains(driver)\
        .click(delevery_cehckbox)\
        .perform()

    # Wait until the Custom Courier Ceckbox Appears then fetch the element
    delevery_courier = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div/label'))
    )
    # Click on Custom Courier
    ActionChains(driver)\
        .click(delevery_courier)\
        .perform()

    # Wait until the Custom Option Selection Appears then fetch the element
    delevery_option = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[1]/div/button'))
    )
    # Click on Custom Option
    ActionChains(driver)\
        .click(delevery_option)\
        .perform()

    # Find Free Shipping Menu
    delevery_free = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[1]/div/div/div/div[2]')
    # Click on Free Shipping Menu
    ActionChains(driver)\
        .click(delevery_free)\
        .perform()

    # Wait until the Delevery Period Selection Appears then fetch the element
    delevery_period = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[2]/button'))
    )
    # Click on Delevery Period Selection
    ActionChains(driver)\
        .click(delevery_period)\
        .perform()

    # Find the Delevery Day Selection
    delevery_day = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[2]/div/div/div[6]')
    # Click on Delevery Day Selection
    ActionChains(driver)\
        .click(delevery_day)\
        .perform()

    # Find the List Now Button
    list_submit = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/div/button')
    # Click on List Now Button
    ActionChains(driver)\
        .click(list_submit)\
        .perform()

    # Wait until the Delevery Period Selection Appears then fetch the element
    success_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/p'))
    )

    # Wait for 10 seconds until the post is listed
    time.sleep(10)
