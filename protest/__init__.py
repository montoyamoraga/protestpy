import os
from os import system
import sys
import time
import string
import random
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def scrape_google_images(subject):


    #print message
    print "open new google chrome window"

    # new driver using google chrome
    driver = webdriver.Chrome()

    # set the window size of the driver
    driver.set_window_size(1200, 800)

    # wait for 5 seconds
    time.sleep(2)

    # url to be scraped
    base_url = "https://www.google.com/search?site=&tbm=isch&source=hp&biw=1044&bih=584&q=pinera&oq="

    #retrieve the argument from the function
    handle = subject

    #reconstruct the complete url
    complete_url = base_url + handle

    #print message
    print "go to google and search for images"

    # go to the url
    driver.get(complete_url)

    # wait for 2 seconds
    time.sleep(2)

    #create folder for storing pics
    system("mkdir pics_" + subject)
    system("cd pics_" + subject)

    # find images
    images = driver.find_elements_by_tag_name("img")

    # reset counter
    counter = 0

    # iterate through all of the images
    for image in images:
        imageSrc = image.get_attribute('currentSrc')
        print imageSrc
        # save the images to the pics folder, as counter.png
        urllib.urlretrieve(imageSrc, "./pics_" + subject + "/" + str(counter) + ".png")
        counter = counter + 1

    #close the browser
    driver.quit()
