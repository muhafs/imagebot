import os
import json
import time
import requests
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
    posts = response.json()['data'][0]

    print(str(total_data) + ' posts has found, this will take a while, please wait...')
    for index, post in enumerate(posts):  # loop over each posts
        # when it reaches 100 posts, then let the machine rest for 5 minutes
        if index % 100 == 0 and index != 0:
            # set the sleep minutes
            sleep_minutes = 5
            # print the rest message
            print(f'Let the machine rest for {sleep_minutes} minutes...')
            # sleep for * minutes
            time.sleep(sleep_minutes * 60)

        sc(post['product_name'], post['product_price'], post['product_seller'])
else:
    print('data not found !')
