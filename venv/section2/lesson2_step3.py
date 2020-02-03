from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    a_s = browser.find_element_by_id("num1")
    a = a_s.text
    num1 = int(a)

    b_s = browser.find_element_by_id("num2")
    b = b_s.text
    num2 = int(b)

    y = str(num1+num2)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(y)  # ищем элемент с текстом "Python"

    button = browser.find_element_by_css_selector("button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
