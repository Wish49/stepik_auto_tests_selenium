from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_1 = browser.find_element(By.ID, "num1")
    x_int1 = int(x_1.text)
    x_2 = browser.find_element(By.ID, "num2")
    x_int2 = int(x_2.text)
    sum_x1_x2 = x_int1+x_int2

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(sum_x1_x2))

    # input1 = browser.find_element(By.CSS_SELECTOR, "#answer")
    # input1.send_keys(y)
    # input2 = browser.find_element(By.ID, "robotCheckbox")
    # input2.click()
    # input3 = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    # input3.click()
        
    button = browser.find_element(By.CSS_SELECTOR, "button")
    button.click()

    time.sleep(1)

    
finally:
    time.sleep(10)
    browser.quit()
