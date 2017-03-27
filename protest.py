# protest.py
# by aaron montoya-moraga

#import stuff
import os
from os import system
import sys
import time
import string
import random
from PIL import Image, ImageDraw, ImageFont

# import selenium module for webscraping
# include webdriver for using chrome and Keys for using keyboard commands
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# retrieve the protestSubject from the terminal
# TODO: catch the exception if the user does not input anything
protestSubject = sys.argv[1]
print protestSubject

handle = protestSubject

# new driver using google chrome
driver = webdriver.Chrome()

# set the window size of the driver
driver.set_window_size(1200, 800)

# variable for going to next page
isNext = True

# url to be scraped
base_url = "https://www.google.com/"

complete_url = base_url + handle

# go to the url
driver.get(complete_url)

# wait for 2 seconds
time.sleep(2)

#print message
print "go to google and retrieve pics"

#find images
images = driver.find_elements_by_tag_name("img")

# iterate through all of the images
for image in images:
    imageSrc = image.get_attribute('currentSrc')
    print imageSrc
    # save the images to the pics folder, as counter.png
    urllib.urlretrieve(imageSrc, "./protest_" + protestSubject + "./pics/" + str(counter) + ".png")
    counter = counter + 1

# wait 5 seconds
time.sleep(5)


prePath = "./pics/"
pngExtension = ".png"
jpgExtension = ".jpg"

#reset counter
counter = 0



driver.quit()
