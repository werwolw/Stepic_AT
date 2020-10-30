from .pages.product_page import ProductPage

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()                     # открываем страницу
    page.add_to_basket()            # выполняем метод страницы — добавляем товар в корзину
    page.should_be_add_item_alert()      # ищем сообщение об упешном добавлении товара в корзину
    page.should_be_price_basket_alert() # сравниваем цену в корзине с сообщением

