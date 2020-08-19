from selenium import webdriver
from selenium.webdriver.support.ui import Select

import time
import math
import os


try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    name = browser.find_element_by_name("firstname")
    name.send_keys("Name")
    l_name = browser.find_element_by_name("lastname")
    l_name.send_keys("Last Name")
    email = browser.find_element_by_name("email")
    email.send_keys("email@example.com")
    file_button = browser.find_element_by_name("file")
    current_dir=os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "empty_file.txt")
    file_button.send_keys(file_path)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#пустая строка