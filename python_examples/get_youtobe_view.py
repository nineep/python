#!/usr/bin/env python

import time
from selenium import webdriver

count = int(raw_input("Number of times to be repeated: "))

x = raw_input("Enter the url (no https): ")
print( "Length of video:")
minutes = int(raw_input("Minutes "))
seconds = int(raw_input("Seconds "))

refreshrate = minutes * 60 + seconds

driver = webdriver.Safari()
driver.get("http://"+x)

for i in range(count):
    time.sleep(refreshrate)
    driver.refresh()
