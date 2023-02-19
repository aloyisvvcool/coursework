from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os
import pyautogui
import time
file_path = ''
caption = ''
LOGIN_EMAIL = "plsgivea1@gmail.com"
LOGIN_PASSWORD = "compa1orcry!"
# Create a new instance of the Edge driver
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

##########
for i in range(8):
    pyautogui.press('tab')
pyautogui.typewrite(caption)
for i in range(30):
    pyautogui.press('tab')
pyautogui.press('enter')
pyautogui.hotkey('command', 'shift', 'g')
time.sleep(2)
pyautogui.typewrite(file_path)
time.sleep(2)
pyautogui.press('enter')
for i in range(33):
    pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(10)