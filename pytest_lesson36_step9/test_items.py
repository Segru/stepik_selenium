import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_button_to_add_to_basket(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "Button not found"
    time.sleep(1)
