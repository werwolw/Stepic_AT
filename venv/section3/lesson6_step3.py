import pytest
from selenium import webdriver
import time
import math



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
    browser.implicitly_wait(5)
    # browser.find_element_by_css_selector(".textarea")
    answer = str(math.log(int(time.time())))
    input = browser.find_element_by_tag_name("textarea")
    input.send_keys(answer)
    button = browser.find_element_by_css_selector(".submit-submission")
    button.click()
    #text_el = WebDriverWait(browser, 10).until(
    #    EC.text_to_be_present_in_element((By.CLASS_NAME, "smart-hints__hint")))
    time.sleep(2)
    text_el = browser.find_element_by_css_selector(".smart-hints__hint")
    assert "Correct!" == text_el.text, "NOT CORRECT!"

    # нужно добавить сравнение сообщения с Correct
