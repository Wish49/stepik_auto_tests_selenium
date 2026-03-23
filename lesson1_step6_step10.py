from selenium import webdriver
from selenium.webdriver.common.by import By
import time 

link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    label = browser.find_elements(By.TAG_NAME, 'label')
    _input = browser.find_elements(By.TAG_NAME, 'input')

    for i,k in enumerate(label):
        k=k.text
        if k[-1]=="*":
            _input[i].send_keys("заполнить")
    #input1 = browser.find_element(By.CSS_SELECTOR, "input.first")
    #input1.send_keys("Ivan")
    #input2 = browser.find_element(By.CSS_SELECTOR, "input.second")
    #input2.send_keys("Petrov")
    #input3 = browser.find_element(By.CSS_SELECTOR, "input.third")
    #input3.send_keys("Smolensk@mail.com")
        
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла