import os
import requests
from tqdm import tqdm  # to show progress bar of download in the command line


# create dounload image function
def download_image(url, dir, param):
    # check if the directory exists
    if not os.path.exists(dir):
        os.makedirs(dir)
    # fetch data from the url
    response = requests.post(url, param)
    # check response status
    if response.status_code == 200 and response.json()['api_status'] == 200:
        # Extract data
        posts = response.json()['data']
        # show total of posts found
        total = response.json()['total_data']
        print(f'{total} posts has found, this will take a while please wait...')
        # loop over each posts
        for product in tqdm(posts):
            # loop over each image
            for i in range(1, 4):
                # fetch the image
                image = requests.get(product['image_url_' + str(i)]).content
                # set the filename
                filename = r"images/" + product['image_name_' + str(i)]
                # save the image
                with open(filename, 'wb') as f:
                    # write the image to the file
                    f.write(image)
    else:
        # print error message
        print('data not found !')
