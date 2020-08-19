from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def calc(x, y):
    return str(int(x) + int(y))

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    num1 = browser.find_element_by_css_selector(".container .nowrap:nth-child(2)").text
    num2 = browser.find_element_by_css_selector(".container .nowrap:nth-child(4)").text
    sum_of_nums = calc(num1, num2)
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(sum_of_nums)

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

#пустая строка