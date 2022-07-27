import os
import json
import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from login_carousell import login_carousell
from download_image import download_image as dl
from scraping_automation import scraping_automation as sc

# set the url api
API_URL = 'https://sindomall.com/api/get-post-product-data-by-region-and-date'
# set the parameters
PARAM = {
    'server_key': 'c36edcc96abfc7f5a07db022f2c3b096',
    'region_name': 'batu',
    'start_date': '2022-07-21',
    'to_date': '2022-07-21'
}
# set directory name to save the image
IMAGE_DIR = 'images'

# # download images
# dl(API_URL, IMAGE_DIR, PARAM)

# # take a rest for 5 minutes
# time.sleep(300)

# Fetch the data from the API
response = requests.post(API_URL, PARAM)

# check response status
if response.status_code == 200 and response.json()['api_status'] == 200:
    # Extract Total data
    total_data = response.json()['total_data']
    # Extract Posts Data
    posts = response.json()['data']

    list_post = [[posts[0]]]

    print(str(total_data) + ' posts found, this will take a while, please wait...')

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('https://www.carousell.sg/sell/')

    # Find Thee Login Button
    search_btn = driver.find_element(
        By.XPATH, '//a[@href="/login"]')
    # Click on the Login Button
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

    for index, post in enumerate(list_post):  # loop over each posts
        # when it reaches 100 posts, then let the machine rest for 5 minutes
        if index % 100 == 0 and index != 0:
            # set the sleep minutes
            sleep_minutes = 5
            # print the rest message
            print(f'Let the machine rest for {sleep_minutes} minutes...')
            # sleep for * minutes
            time.sleep(sleep_minutes * 60)

        # sc(post['product_name'], int(
        #     post['product_price']), post['product_seller'])

        # Find the upload file button
        for i in range(1, 4):
            # Wait until the page is loaded then fetch the element
            upload_btn = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located(
                    (By.XPATH, '//input[@accept="image/png, image/jpeg" and @type="file"]'))
            )
            # insert / upload files
            upload_btn.send_keys(
                'C:/Users/62851/Desktop/Projects/imagebot/images/' + post[0]['post_id'] + '_' + str(i) + '.jpg')  # ! Images

        time.sleep(5)

        # Find the Category Selection
        category_select = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div')
        # Click on category selection to dropdown menu
        ActionChains(driver)\
            .click(category_select)\
            .perform()

        time.sleep(5)

        # Find the Category Search Bar
        category_search = driver.find_element(
            By.XPATH, '//input[@type="text" and @placeholder="Search for a category..."]')
        # Enter the category
        category_search.send_keys('Plants & Seeds')

        time.sleep(5)

        # Find the Plants & Seeds Menu
        plants_menu = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]')
        # Click on category selection to dropdown menu
        ActionChains(driver)\
            .click(plants_menu)\
            .perform()

        time.sleep(5)

        # Wait until the Listing Title Bar Appears then fetch the element
        listing_title = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//input[@type="text" and @name="field_title" and @placeholder="Name your listing"]'))
        )
        # Enter the Listing Title
        listing_title.send_keys(post[0]['product_name'])  # ! Title

        time.sleep(5)

        # Find the New Conditional Checkbox
        plants_menu = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[4]/div[2]/div/div/div[1]')
        # Click on New Conditional Checkbox
        ActionChains(driver)\
            .click(plants_menu)\
            .perform()

        time.sleep(5)

        # Find the Price Bar
        listing_price = driver.find_element(
            By.XPATH, '//input[@type="number" and @name="field_price" and @placeholder="Price of your listing"]')
        # Enter the Price
        listing_price.send_keys(int(post[0]['product_price']))  # ! Price

        time.sleep(5)

        # Find the Description Bar
        listing_desc = driver.find_element(
            By.XPATH, '//textarea[@name="field_description"]')
        # Enter the Description
        listing_desc.send_keys(
            'Indoor plant\nEasy maintenance\n\nPlease chat to check its availability.\nThank you and happy shopping!\n\n' + post[0]['product_seller'])  # ! Description

        # time.sleep(5)

        # # Find the Delevery Cehckbox
        # delevery_cehckbox = driver.find_element(
        #     By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/label')
        # # Click on Delevery Cehckbox
        # ActionChains(driver)\
        #     .click(delevery_cehckbox)\
        #     .perform()

        # time.sleep(5)

        # # Wait until the Custom Courier Ceckbox Appears then fetch the element
        # delevery_courier = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div/label'))
        # )
        # # Click on Custom Courier
        # ActionChains(driver)\
        #     .click(delevery_courier)\
        #     .perform()

        # time.sleep(5)

        # # Wait until the Custom Option Selection Appears then fetch the element
        # delevery_option = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[1]/div/button'))
        # )
        # # Click on Custom Option
        # ActionChains(driver)\
        #     .click(delevery_option)\
        #     .perform()

        # time.sleep(5)

        # # Find Free Shipping Menu
        # delevery_free = driver.find_element(
        #     By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[1]/div/div/div/div[2]')
        # # Click on Free Shipping Menu
        # ActionChains(driver)\
        #     .click(delevery_free)\
        #     .perform()

        # time.sleep(5)

        # # Wait until the Delevery Period Selection Appears then fetch the element
        # delevery_period = WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located(
        #         (By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[2]/button'))
        # )
        # # Click on Delevery Period Selection
        # ActionChains(driver)\
        #     .click(delevery_period)\
        #     .perform()

        # time.sleep(5)

        # # Find the Delevery Day Selection
        # delevery_day = driver.find_element(
        #     By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[2]/div/div/div[6]')
        # # Click on Delevery Day Selection
        # ActionChains(driver)\
        #     .click(delevery_day)\
        #     .perform()

        time.sleep(5)

        # Find the List Now Button
        list_submit = driver.find_element(
            By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/div/button')
        # Click on List Now Button
        ActionChains(driver)\
            .click(list_submit)\
            .perform()

        time.sleep(5)

        # Wait until the Success Message Appears then fetch the element
        success_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, '//*[@id="root"]/div/div[2]/div[1]/div[2]/div[1]/p'))
        )

        # Wait for 10 seconds before windows closes
        time.sleep(10)
else:
    print('data not found !')
