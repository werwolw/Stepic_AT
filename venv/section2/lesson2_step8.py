from selenium import webdriver
import os
import time
try:
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    f_name = browser.find_element_by_name("firstname")
    f_name.send_keys("Kostyan")
    l_name = browser.find_element_by_name("lastname")
    l_name.send_keys("Shiryaev")
    email = browser.find_element_by_name("email")
    email.send_keys("adc@ya.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    imp_f = browser.find_element_by_id("file")
    imp_f.send_keys(file_path)
    # print(os.path.abspath(__file__))
    # print(os.path.abspath(os.path.dirname(__file__)))

    button = browser.find_element_by_css_selector("button.btn")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
