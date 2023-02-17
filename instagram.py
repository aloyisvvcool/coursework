                               
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
FILE_PATH = "/Users/snyper/Downloads/testfile.png"
CAPTION = "THIS IS A TEST"
# Create a new instance of the Chrome driver
driver = webdriver.Edge()

print("section 2")

# Navigate to Instagram website
driver.get("https://www.instagram.com/")                             
time.sleep(10)

# Press the tab key 2 times
for i in range(2):
    pyautogui.press('tab')

pyautogui.typewrite(LOGIN_EMAIL)
pyautogui.press('tab')
pyautogui.typewrite(LOGIN_PASSWORD)
pyautogui.press('enter')

time.sleep(10)
# press the tab key 8 times
for i in range(8):
    pyautogui.press('tab')
time.sleep(2)
pyautogui.press('enter')
time.sleep(20)



'''


EVERYTHING BELOW HERE IS NOT TESTED


'''
# Find the file input element and send the file path
pyautogui.press('tab')
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('command', 'shift', 'g')
time.sleep(2)
pyautogui.typewrite(FILE_PATH)
time.sleep(2)
pyautogui.press('enter')
time.sleep(2)
for i in range(2):
    pyautogui.press('tab')
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
for i in range(5):
    pyautogui.press('tab')
pyautogui.typewrite(CAPTION)
pyautogui.hotkey('shift', 'tab')
pyautogui.hotkey('shift', 'tab')
pyautogui.press('enter')

time.sleep(30)