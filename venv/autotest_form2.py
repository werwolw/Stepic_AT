from selenium import webdriver
import time

link = "http://master.boquar.com/login"

browser = webdriver.Chrome()
browser.get(link)

try:
    # Ищем форму ввода логина по ID
    login = browser.find_element_by_id("mat-input-0")
    # Делаем клик в поле логина
    login.click()
    # Клик в пустом месте
    browser.find_element_by_xpath("//html").click()
    # Ждем 1 сек (для наглядности)
    time.sleep(1)
    # ищем текст ошибки
    # error_text_elt_lg = browser.find_element_by_css_selector("#mat-error-0 .ng-star-inserted")
    # error_text_lg = error_text_elt_lg.text
    # Сравниваем найденный текст ошибки с ожидаемым
    # assert "Это обязательно поле" == error_text_lg, "Сообщение не совпадает с ожидаемым"

    # Ищем форму ввода пароля с помощью Xpath (можно и по ID "mat-input-1")
    pwd = browser.find_element_by_xpath("//input[@formcontrolname='password']")
    # Делаем клик в поле пароля
    pwd.click()
    # Клик в пустом месте
    browser.find_element_by_xpath("//html").click()
    # Ждем 1 сек (для наглядности)
    time.sleep(1)
    # ищем текст ошибки
    # error_text_elt_pwd = browser.find_element_by_css_selector("#mat-error-1>.ng-star-inserted")
    # error_text_pwd = error_text_elt_pwd.text
    # Сравниваем найденный текст ошибки с ожидаемым
    #assert "Это обязательне поле" == error_text_lg, "Сообщение не совпадает с ожидаемым"

    # Ищем кнопку Войти
    button = browser.find_element_by_css_selector("button")
    btn_cheked = button.get_attribute("disabled")
    # Проверяем ее доступность
    if btn_cheked == "true":
        browser.execute_script("alert('Кнопка Не активна и это хорошо')")
    else:
        browser.execute_script("alert('Кнопка активна и это плохо!')")
    # assert btn_cheked == "true", "Ошибка! Кнопка должна быть недоступна!"     # как вариант через assert
    time.sleep(1)

finally:
    # ждем 5 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла