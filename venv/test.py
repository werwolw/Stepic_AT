import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait

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
    def test_login_3(self, browser):
        # Открываем страницу в браузере
        browser.get(link)
        # Ищем ссылку на stackoverflow и переходим по ней
        link_stack = browser.find_element_by_xpath("//a[text()='stackoverflow']")
        link_stack.click()
        # Ждем, когда загрузится страница stackoverflow
        title = WebDriverWait(browser, 5).until(EC.title_contains("Stack"))
        assert title, "Это не стак"

    # не забываем оставить пустую строку в конце файла