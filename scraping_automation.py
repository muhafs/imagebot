import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get('https://www.google.com/')

search_box = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
time.sleep(3)
search_box.send_keys('Hello World')

search_button = driver.find_element_by_xpath(
    '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[3]/center/input[1]').click()
search_button.click()
