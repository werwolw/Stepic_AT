from .pages.product_page import ProductPage
import pytest

# link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


@pytest.mark.parametrize('promo_offer', ["0", "1", "3", "4", "5", "6",
                         pytest.param("7", marks=pytest.mark.xfail(reason="some bug")), # помечаем ссылку как ожидаемый баг
                                         "8", "9"])
def test_guest_can_add_product_to_basket(browser, promo_offer):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{promo_offer}"
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.add_to_basket()            # выполняем метод страницы — добавляем товар в корзину
    page.should_be_add_item_alert()      # ищем сообщение об упешном добавлении товара в корзину
    page.should_be_price_basket_alert() # сравниваем цену в корзине с сообщением

