from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://SunInJuly.github.io/execute_script.html"
#browser = webdriver.Chrome()
#browser.get(link)
try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
            
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    time.sleep(1)

    
finally:
    time.sleep(10)
    browser.quit()
