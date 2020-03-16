import unittest
from selenium import webdriver
import time

class Test_Input(unittest.TestCase):
    def test_input1(self):

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block>.first_class>input")
        input1.send_keys("ответ")
        ##здесь упадет на втором сайте, так как нет елемента .second_class
        input2 = browser.find_element_by_css_selector(".first_block>.second_class>input")
        input2.send_keys("ответ")

        input1 = browser.find_element_by_css_selector(".first_block>.third_class>input")
        input1.send_keys("ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text not compare")

    def test_input2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector(".first_block>.first_class>input")
        input1.send_keys("ответ")
        ##здесь упадет на втором сайте, так как нет елемента .second_class
        input2 = browser.find_element_by_css_selector(".first_block>.second_class>input")
        input2.send_keys("ответ")

        input1 = browser.find_element_by_css_selector(".first_block>.third_class>input")
        input1.send_keys("ответ")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        # assert "Congratulations! You have successfully registered!" == welcome_text

        # ожидание чтобы визуально оценить результаты прохождения скрипта
        time.sleep(5)
        # закрываем браузер после всех манипуляций
        browser.quit()
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "Text not compare")


if __name__ == "__main__":
    unittest.main()
