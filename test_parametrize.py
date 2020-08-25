import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import math
import time


def calc():
    return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.mark.parametrize('link_num', ["236895","236896", "236897","236898","236899","236903","236904","236905"])
def test_check_correct(browser, link_num):
    link = f"https://stepik.org/lesson/{link_num}/step/1"
    browser.get(link)
    input_for_answer = WebDriverWait(browser,5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.textarea.ember-view'))
    )    
    input_for_answer.send_keys(calc())
    button = WebDriverWait(browser,5).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.submit-submission'))
    )
    button.click()
    correct = WebDriverWait(browser, 10).until(EC.visibility_of_element_located((By.CSS_SELECTOR, '.smart-hints__hint'))).text
    #correct = browser.find_element_by_css_selector('.smart-hints__hint').text
    assert correct == "Correct!"
