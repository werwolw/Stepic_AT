from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math
import  time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    # говорим Selenium проверять в течение 12 секунд, пока текст не станет $100
    button = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    button = browser.find_element_by_id("book") # затем жмем кнопку
    button.click()

    # код для капчи
    search_x = browser.find_element_by_id("input_value")
    a = search_x.text
    x = int(a)
    func_res = str(math.log(abs(12 * math.sin(x))))  # считаем функцию
    answer = browser.find_element_by_id("answer")  # находим поле для ввода
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(func_res)  # вводим ответ

    button = browser.find_element_by_id("solve")
    button.click()
finally:
    time.sleep(10)
    browser.quit()