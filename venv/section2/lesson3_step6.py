from selenium import webdriver
import time
import math
try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    but1 = browser.find_element_by_css_selector("button.trollface")
    but1.click()

    new_window = browser.window_handles[1]   # узнаем имя новой вкладки
    browser.switch_to.window(new_window)     # переключаемся на новую вкладку

    x_str = browser.find_element_by_id("input_value")
    x_text = x_str.text
    x_int = int(x_text)

    func = str(math.log(abs(12 * math.sin(x_int))))
    answer = browser.find_element_by_id("answer")
    answer.send_keys(func)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(8)
    # закрываем браузер после всех манипуляций
    browser.quit()