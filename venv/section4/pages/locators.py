from selenium.webdriver.common.by import By


class ProductPageLocators:
    btn_add_to_bkt = (By.CSS_SELECTOR, ".btn-add-to-basket")
    item_name = (By.CSS_SELECTOR, ".product_main h1")
    price_item = (By.CSS_SELECTOR, ".product_main .price_color")
    add_txt_msg = (By.CSS_SELECTOR, ".alertinner strong")
    price_bkt_msg = (By.CSS_SELECTOR, ".alertinner p strong")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
