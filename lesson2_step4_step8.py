from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()

browser.get("http://suninjuly.github.io/explicit_wait2.html")

button = WebDriverWait(browser, 12).until(
        EC.element_to_be_clickable((By.ID, "book"))
    )

is_text = WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element(
        (By.ID, "price"), "$100"))
if is_text == True:
    
    button.click()
# #message = browser.find_element(By.ID, "verify_message")
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)
# #assert "successful" in message.text
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    button = browser.find_element(By.ID, "solve")
    button.click()

time.sleep(10)

browser.quit()
