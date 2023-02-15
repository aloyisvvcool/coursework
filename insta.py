from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import pyautogui
import time
import urllib.request


LOGIN_EMAIL = "plsgivea1@gmail.com"
LOGIN_PASSWORD = "43w tg534tgi537 bgv34"
# Create a new instance of the Chrome driver
driver = webdriver.Edge()

# Navigate to TikTok website
driver.get("https://www.instagram.com/")
time.sleep(10)

#login
time.sleep(5)

username = driver.find_element(By.XPATH, "input[name='username']")
password = driver.find_element(By.XPATH, "input[name='password']")
username.clear()
password.clear()
username.send_keys(LOGIN_EMAIL)
password.send_keys(LOGIN_PASSWORD)
login = driver.find_element_by_css_selector("button[type='submit']").click()

#save your login info?
time.sleep(10)
notnow = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
#turn on notif
time.sleep(10)
notnow2 = driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()

time.sleep(10)

'''


EVERYTHING BELOW HERE IS NOT TESTED


'''
# Find the file input element and send the file path
file_input = driver.find_element_by_xpath("//input[@type='file']")
file_input.send_keys(os.path.abspath("path/to/your/video.mp4"))

# Wait for the video to upload and fill in the video details and post it
WebDriverWait(driver, 120).until(EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Post')]")))

# Fill in the video details and post it
title_input = driver.find_element_by_xpath("//input[@placeholder='Add a caption (optional)']")
title_input.send_keys("My awesome video")
post_button = driver.find_element_by_xpath("//button[contains(text(), 'Post')]")
post_button.click()
