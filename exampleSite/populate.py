import urllib.request
import random
from faker import Faker

RANDOM_IMG_URL = "https://picsum.photos/{}/{}/?random"
MIN = 400
MAX = 1000
NB_IMG = 30
DIR_IMG = "static/images/"
MD_DIR = "content/gallery/"
img_template = """
+++
date = "{}-{}-{}T00:00:00-00:00"
title = "{}"
tags = []
categories = []
img_name = "{}"
place = "{}"
coordinates = ["{}","{}"]
headless = true
display_location = true
+++

{}
"""


def get_random_img(filename):
    urllib.request.urlretrieve(RANDOM_IMG_URL.format(random.randint(MIN,MAX),random.randint(MIN,MAX)), DIR_IMG + filename)


def generate_data():
    fake = Faker()
    for k in range(NB_IMG):
        filename = "img{}.jpeg".format(k)
        print("Getting {}...".format(filename))
        
        title = fake.sentence().replace('.','')
        longitude = random.randint(0, 50)
        latitude = random.randint(45, 60)
        text = ""
        year = random.randint(2010, 2018)
        month = random.randint(1, 12)
        day = random.randint(1, 28)

        if random.randint(0,1):
            text = fake.paragraph()

        # generate a .md file 
        text = img_template.format(year, str(month).zfill(2), str(day).zfill(2), title, filename, "Some place", longitude, latitude, text)
        md_file = open(MD_DIR + title.replace(' ','_')+'.md','w')
        md_file.write(text)
        
        # download an image
        #get_random_img(filename)
        md_file.close()


generate_data()
