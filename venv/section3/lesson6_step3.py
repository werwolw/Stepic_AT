import pytest
from selenium import webdriver
import time
import math


@pytest.fixture(scope="function")
def browser():
    answer = math.log(int(time.time()))
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('site', [
    "https://stepik.org/lesson/236895/step/1",
    "https://stepik.org/lesson/236896/step/1",
    "https://stepik.org/lesson/236897/step/1",
    "https://stepik.org/lesson/236898/step/1",
    "https://stepik.org/lesson/236899/step/1",
    "https://stepik.org/lesson/236903/step/1",
    "https://stepik.org/lesson/236904/step/1",
    "https://stepik.org/lesson/236905/step/1"
    ])
def test_search_Correct(browser, site):
    browser.get(site)
    browser.find_element_by_tag_name("textarea")
    answer = math.log(int(time.time()))
    input = browser.find_element_by_tag_name("textarea")
    input.send_keys(answer)
    # нужно добавить сравнение сообщения с Correct