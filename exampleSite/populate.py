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
date = "2018-01-01T00:00:00-00:00"
title = "{}"
tags = []
categories = []
img_name = "{}"
place = "{}"
coordinates = ""
headless = true
+++
"""


def get_random_img(filename):
    urllib.request.urlretrieve(RANDOM_IMG_URL.format(random.randint(MIN,MAX),random.randint(MIN,MAX)), DIR_IMG + filename)


def generate_data():
    fake = Faker()
    for k in range(NB_IMG):
        filename = "img{}.jpeg".format(k)
        print("Getting {}...".format(filename))
        
        title = fake.sentence().replace('.','')
        
        # generate a .md file 
        text = img_template.format(title, filename, "Some place")
        md_file = open(MD_DIR + title.replace(' ','_')+'.md','w')
        md_file.write(text)
        
        # download an image
        get_random_img(filename)
        md_file.close()


generate_data()
