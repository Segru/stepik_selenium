from selenium import webdriver

import math
import time

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    blue_button = browser.find_element_by_tag_name("button")
    blue_button.click()
    confirm = browser.switch_to.alert
    confirm.accept()

    x = browser.find_element_by_id("input_value").text
    y = calc(x)
    input_y = browser.find_element_by_css_selector(".form-control")
    input_y.send_keys(y)
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:
        # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#пустая строка