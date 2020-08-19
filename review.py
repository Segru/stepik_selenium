from selenium import webdriver
import time 

link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)


    f_name = browser.find_element_by_css_selector(".first_block .first")
    f_name.send_keys("Ivan")
    l_name = browser.find_element_by_css_selector(".first_block .second")
    l_name.send_keys("Petrov")
    email = browser.find_element_by_css_selector(".first_block .third")
    email.send_keys("example@example.com")
    phone = browser.find_element_by_css_selector(".second_block .first")
    phone.send_keys("123456789")
    address = browser.find_element_by_css_selector(".second_block .second")
    address.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
