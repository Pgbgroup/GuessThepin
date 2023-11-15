from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver without specifying executable_path
driver = webdriver.Chrome()

# Replace 'https://www.instagram.com' with the URL of the Instagram login page
driver.get('https://www.guessthepin.com/')


input_element = driver.find_element("id", "pin")  # Replace "your_input_id" with the actual ID of the input field
a=[f'{i:04d}' for i in range(10000)]
for j in a:
    input_element = driver.find_element("id", "pin")
    input_element.send_keys(j)
    input_element.send_keys(Keys.ENTER)
