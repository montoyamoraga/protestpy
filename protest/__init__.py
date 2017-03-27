import os
from os import system
import sys
import time
import string
import random
from PIL import Image, ImageDraw, ImageFont
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def protest(subject):
    protestSubject = subject

def scrape_google():
    # new driver using google chrome
    driver = webdriver.Chrome()

    # set the window size of the driver
    driver.set_window_size(1200, 800)

    # wait for 5 seconds
    time.sleep(5)

    driver.quit()
