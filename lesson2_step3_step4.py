from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    input1 = browser.find_element(By.CSS_SELECTOR, ".btn")
    input1.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
                
    button = browser.find_element(By.CSS_SELECTOR, ".btn-primary")
    button.click()

    time.sleep(1)

    
finally:
    time.sleep(10)
    browser.quit()
