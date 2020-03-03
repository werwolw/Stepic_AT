from selenium import webdriver
import time
import math
link = "https://suninjuly.github.io/execute_script.html"
try:
    browser = webdriver.Chrome()
    browser.get(link)
    search_x = browser.find_element_by_id("input_value")
    a = search_x.text
    x = int(a)

    func_res = str(math.log(abs(12*math.sin(x)))) #считаем функцию
    answer = browser.find_element_by_id("answer")  #находим поле для ввода
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(func_res)  #вводим ответ

    ch_b = browser.find_element_by_id("robotCheckbox") #ищем чекбокс и отмечаем его
    ch_b.click()
    rd_b = browser.find_element_by_id("robotsRule")  #ищем радиобаттон и кликаем
    #browser.execute_script("return arguments[0].scrollIntoView(true);", rd_b)
    rd_b.click()

    button = browser.find_element_by_tag_name("button")
    #browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
