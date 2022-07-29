import os
import shutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import chromedriver_binary  # ini untuk dia ga langsung berhenti
import urllib.request
import requests


options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
home_directory = os.getcwd()+"/"
options.add_argument("user-data-dir=" + home_directory + "/cookies")
driver = webdriver.Chrome(options=options, service=Service(
    ChromeDriverManager().install()))


# # First Download Image
URL = "https://sindomall.com/api/get-post-product-data-by-region-and-date"
data = {
    "server_key": "c36edcc96abfc7f5a07db022f2c3b096",
    "region_name": "batu",
    "start_date": "2022-07-27",
    "to_date": "2022-07-27"
}

r = requests.post(url=URL, data=data)

data = r.json()
products = data['data']
# # List Nama Gambar
# listNamaGambar1 = []
# listNamaGambar2 = []
# listNamaGambar3 = []

# # List Image Url
# listGambar1 = []
# listGambar2 = []
# listGambar3 = []

# List Post Carousel
listPostId = []
listProductName = []
listPrice = []
listSellerName = []

# # Pertama, download gambar dulu
# for index, json in enumerate(products):
#     # Download Gambar 1
#     listGambar1.append(json['image_url_1'])
#     listNamaGambar1.append(json['image_name_1'])
#     urllib.request.urlretrieve(
#         listGambar1[index], format(listNamaGambar1[index]))
#     time.sleep(3)

#     # Download Gambar 2
#     listGambar2.append(json['image_url_2'])
#     listNamaGambar2.append(json['image_name_2'])
#     urllib.request.urlretrieve(
#         listGambar2[index], format(listNamaGambar2[index]))
#     time.sleep(3)

#     # Download Gambar 3
#     listGambar3.append(json['image_url_3'])
#     listNamaGambar3.append(json['image_name_3'])
#     urllib.request.urlretrieve(
#         listGambar3[index], format(listNamaGambar3[index]))
#     time.sleep(3)

#     # time.sleep(3)
#     print('index sekarang', format(index))
# print('selesai')

# # Login Carousel dulu jika belum login
# driver.get(
#     "https://www.carousell.sg/")
# time.sleep(2)
# loginButton = driver.find_element(
#     By.XPATH, '//a[@href="/login"]')
# loginButton.click()

# time.sleep(2)

# username = driver.find_element(
#     By.XPATH, '//input[@name="username"]')
# username.send_keys('tetanggakita')
# time.sleep(2)
# password = driver.find_element(
#     By.XPATH, '//input[@name="password"]')
# password.send_keys('Ph1lodendron')
# time.sleep(2)
# masuk = driver.find_element(By.XPATH, '//button[text()="Log in"]')
# masuk.click()
# time.sleep(60)


for index, json in enumerate(products):
    driver.get("https://www.carousell.sg")
    time.sleep(1)
    driver.get("https://www.carousell.sg/sell/")
    time.sleep(3)
    listPostId.append(json['post_id'])
    listPrice.append(json['product_price'])
    listProductName.append(json['product_name'])
    listSellerName.append(json['product_seller'])

    for i in range(3):
        imageDir = home_directory + \
            format(listPostId[index]) + "_" + format(i + 1) + ".jpg"
        time.sleep(3)

        dirImage = imageDir.replace("/", "\\")
        sendimage = driver.find_element(By.XPATH, '//input[@type="file"]')
        sendimage.send_keys(dirImage)
    time.sleep(3)

    # CLICK Category
    category = driver.find_element(
        By.XPATH, '//p[text()="Select a category"]')
    category.click()
    time.sleep(3)

    # Search Category
    fillCategory = driver.find_element(
        By.XPATH, '//input[@placeholder="Search for a category..."]')
    time.sleep(1)
    fillCategory.send_keys("Plants")
    time.sleep(3)

    # Select Category
    selectCategory = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div/div[2]/div[2]')
    selectCategory.click()
    time.sleep(3)

    # Write Title
    sendtitle = driver.find_element(By.XPATH, '//input[@name="field_title"]')
    sendtitle.send_keys(listProductName[index])
    time.sleep(3)

    # Click Condition
    condition = driver.find_element(By.XPATH, '//p[text()="New"]')
    condition.click()
    time.sleep(3)

    # Write Price
    sendprice = driver.find_element(By.XPATH, '//input[@name="field_price"]')
    sendprice.send_keys(format(listPrice[index]))
    time.sleep(3)

    # Write Description
    sendDescription = driver.find_element(
        By.XPATH, '//textarea[@name="field_description"]')
    sendDescription.send_keys(
        "Please chat to check its availability. Thank you and happy shopping!\n\n" + listSellerName[index])
    time.sleep(3)

# Jika sudah login, komennya dibiarin aja
#     # # Click Delivery
#     # delivery = driver.find_element(By.XPATH, '//p[text()="Delivery"]')
#     # delivery.click()
#     # time.sleep(1)

#     # # Hit Custom Courier
#     # courier = driver.find_element(By.XPATH, '//p[text()="Custom courier"]')
#     # courier.click()
#     # time.sleep(1)

#     # # Click Custom Courier
#     # custom = driver.find_element(
#     #     By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[1]/div/button/div/span[text()="Custom"]')
#     # custom.click()
#     # time.sleep(1)

#     # # Click Free Shipping
#     # free = driver.find_element(By.XPATH, '//p[text()="Free Shipping"]')
#     # free.click()
#     # time.sleep(1)

#     # # Click duration
#     # duration = driver.find_element(
#     #     By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[2]/button/span[text()="Delivery period (working days)"]')
#     # duration.click()
#     # time.sleep(1)

#     # # Click 6 Days
#     # number6 = driver.find_element(
#     #     By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/section/div[6]/div[3]/div[1]/div[4]/div[2]/div/div/div[6]/p[text()="6"]')
#     # number6.click()
#     # time.sleep(1)
# Jika sudah login biarin saja yang diatas

    # Click Submit
    submit = driver.find_element(
        By.XPATH, '//*[@id="root"]/div/div[2]/div/div[2]/div[2]/div[2]/form/div/button[text()="List now"]')
    submit.click()
    time.sleep(60)
    print('index sekarang : ', index)

print('FINISH UPLOAD POSTING CAROUSEL')
