from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    x_el= browser.find_element_by_id("input_value")
    x = x_el.text
    y = calc(x)
    input_captcha = browser.find_element_by_id("answer")
    input_captcha.send_keys(y)
    button = browser.find_element_by_css_selector("button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    checkbox = browser.find_element_by_css_selector("[for = 'robotCheckbox']")
    checkbox.click()
    radiobutton = browser.find_element_by_css_selector("[for = 'robotsRule']")
    radiobutton.click()
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#пустая строка