from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import os

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

# Navigate to TikTok website
driver.get("https://www.tiktok.com/")

# Wait for the upload button to be visible and click on it
upload_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//button[@aria-label='Upload']")))
upload_button.click()

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
