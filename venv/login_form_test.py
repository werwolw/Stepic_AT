import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time

link = "http://master.boquar.com/login"


@pytest.fixture
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    # этот код выполнится после завершения теста
    print("\nquit browser..")
    browser.quit()


class TestLoginPage:
    def test_login_1(self, browser):    # Проверка входа при незаполненном логине и пароле
        # Открываем страницу в браузере
        browser.get(link)
        # Ищем форму ввода логина по ID
        login = browser.find_element_by_id("mat-input-0")
        # Делаем клик в поле логина
        login.click()
        # Клик в пустом месте
        browser.find_element_by_xpath("//html").click()
        # Ждем 1 сек (для наглядности)
        time.sleep(1)

        # Ищем форму ввода пароля с помощью Xpath (можно и по ID "mat-input-1")
        pwd = browser.find_element_by_xpath("//input[@formcontrolname='password']")
        # Делаем клик в поле пароля
        pwd.click()
        # Клик в пустом месте
        browser.find_element_by_xpath("//html").click()
        # Ждем 1 сек (для наглядности)
        time.sleep(1)

        # Ищем кнопку Войти
        button = browser.find_element_by_css_selector("button")
        # Проверяем ее доступность
        assert button.get_attribute("disabled") == "true", "Кнопка должна быть недоступна!"
        time.sleep(1)

    def test_login_2(self, browser):    # Проверка авторизации при вводе неверных учетных данных
        # Открываем страницу в браузере
        browser.get(link)
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
        button.click()
        time.sleep(1)

        # ищем текст ошибки
        error_text_elt = browser.find_element_by_css_selector("#mat-error-0 .ng-star-inserted")
        # Сравниваем найденный текст ошибки с ожидаемым (тест упадет - специально)
        assert error_text_elt.text == "Неправильное имя пользователя или пароль", "Сообщение не совпадает с ожидаемым!"

    def test_login_3(self, browser):    # проверка актуальности ссылки на stackoverflow
        # Открываем страницу в браузере
        browser.get(link)
        # Ищем ссылку на stackoverflow и переходим по ней
        link_stack = browser.find_element_by_xpath("//a[text()='stackoverflow']")
        link_stack.click()
        # Ждем, когда загрузится страница stackoverflow
        title = WebDriverWait(browser, 5).until(EC.title_contains("Stack Overflow"))
        assert title, "Это не Stackoverflow!"

    # не забываем оставить пустую строку в конце файла
