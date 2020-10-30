from .locators import BasketPageLokators
from .base_page import BasePage


class BasketPage(BasePage):
    # проверка, что корзина пустая
    def should_be_empty_basket_message(self):
        # получаем текст элемента для проверки
        empty_message_txt = self.browser.find_element(*BasketPageLokators.empty_basket_text).text
        assert "empty" in empty_message_txt, \
            "Message of empty basket not presented or basket not empty"

