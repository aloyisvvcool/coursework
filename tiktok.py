from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import pyautogui
import time

LOGIN_EMAIL = "plsgivea1@gmail.com"
LOGIN_PASSWORD = "compa1orcry!"
# Create a new instance of the Chrome driver
driver = webdriver.Edge()

# Navigate to TikTok website
driver.get("https://www.tiktok.com/")
time.sleep(2)
# Click on the login button
login_button = driver.find_element(By.XPATH, '//button[text()="Log in"]')
login_button.click()

time.sleep(1)
# Press the tab key 3 times
for i in range(3):
    pyautogui.press('tab')

# Press the enter key
pyautogui.press('enter')

for i in range(2):
    pyautogui.press('tab')
pyautogui.press('enter')
# Press the tab key 3 times
for i in range(3):
    pyautogui.press('tab')

# Press the enter key
pyautogui.press('enter')

pyautogui.typewrite(LOGIN_EMAIL)
pyautogui.press('tab')
pyautogui.typewrite(LOGIN_PASSWORD)
pyautogui.press('enter')

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
