import pytest

from .pages.main_page import MainPage
from .pages.basket_page import BasketPage

link = "http://selenium1py.pythonanywhere.com/"

@pytest.mark.skip
def test_guest_can_go_to_login_page(browser):
    page = MainPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.go_to_login_page()  # выполняем метод страницы — переходим на страницу логина

@pytest.mark.skip
def test_guest_should_see_login_link(browser):
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()

# проверка пустой корзины при переходе с главной страницы
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_empty_basket_message()
