import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_button_add_to_cart_pass(browser):
    browser.get(link)
    time.sleep(3)
    button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert button, "кнопка не найдена"