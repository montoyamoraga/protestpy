import os
from os import system
import sys
import time
import string
import random
import urllib
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

    #print message
    print "create folders for storing pics"

    #create folder for storing pics
    picsFolder = "pics_" + subject
    system("mkdir " + picsFolder)
    system("cd " + picsFolder)

    #print message
    print "find all of the images"

    # find images
    images = driver.find_elements_by_tag_name("img")

    # reset counter
    counter = 0

    #print message
    print "download every image"

    # iterate through all of the images
    for image in images:
        imageSrc = image.get_attribute('currentSrc')
        print imageSrc
        # save the images to the pics folder, as counter.png
        urllib.urlretrieve(imageSrc, "./pics_" + subject + "/" + str(counter) + ".png")
        counter = counter + 1

    #print message
    print "close browser"

    #close the browser
    driver.quit()
