from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/file_input.html"

current_dir = os.path.abspath(os.path.dirname(__file__))
file_name = "123.txt"
file_path = os.path.join(current_dir, file_name)

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    # x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    # x = x_element.text
    # y = calc(x)

    input1 = browser.find_element(By.NAME, "firstname")
    input1.send_keys("Petro")
    input2 = browser.find_element(By.NAME, "lastname")
    input2.send_keys("petro")
    input3 = browser.find_element(By.NAME, "email")
    input3.send_keys("qwe@qwe.com")
    input4 = browser.find_element(By.ID, "file")
    input4.send_keys(file_path)
            
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    time.sleep(1)

    
finally:
    time.sleep(10)
    browser.quit()
