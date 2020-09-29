from selenium import webdriver
import time

link = "http://master.boquar.com/login"

browser = webdriver.Chrome()
browser.get(link)

try:
    # Ищем форму ввода логина по ID
    login = browser.find_element_by_id("mat-input-0")
    # Вводим логин
    login.send_keys("Ivan")
    # Ждем 1 сек (для наглядности)
    time.sleep(1)

    # Ищем форму ввода пароля с помощью Xpath (можно и по ID "mat-input-1")
    pwd = browser.find_element_by_xpath("//input[@formcontrolname='password']")
    # Вводим пароль
    pwd.send_keys("123456")
    # Ждем 1 сек (для наглядности)
    time.sleep(1)

    # Ищем кнопку Войти
    button = browser.find_element_by_tag_name("button")
    # button = browser.find_element_by_xpath("//span[text()='Войти']") # как вариант
    button.click()
    time.sleep(1)

    # ищем текст ошибки
    error_text_elt = browser.find_element_by_css_selector("#mat-error-0 .ng-star-inserted")
    # error_text = error_text_elt.text

    # Сравниваем найденный текст ошибки с ожидаемым
    assert error_text_elt.text == "Неправильное имя пользователя или пароль, попробуйте еще раз", "Сообщение не совпадает с ожидаемым"


finally:
    # ждем 5 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла