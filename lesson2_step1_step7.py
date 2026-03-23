from selenium import webdriver
from selenium.webdriver.common.by import By
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element(By.CSS_SELECTOR, "#treasure")
    x = x_element.get_attribute("valuex")
    y = calc(x)

    input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    input1.send_keys(y)
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    input3.click()
        
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    time.sleep(1)

    
finally:
    time.sleep(10)
    browser.quit()
