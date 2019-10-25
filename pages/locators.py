# Классы локаторы для Page Object

from selenium.webdriver.common.by import By

class MainPageLocators():
    # каждый селектор — это пара: как искать и что искать
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')


class ProductPageLocators():
    PRODUCT_BUTTON = (By.CSS_SELECTOR, ".add-to-basket")
    #BASKET_VALUE = (By.CSS_SELECTOR, ".basket-mini strong")
    #PRICE_PRODUCT = (By.CSS_SELECTOR, "#content .product_page .product_main .price_color")
    #NAME_PRODUCT = (By.CSS_SELECTOR, "#content .product_page .product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main .price_color")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    #MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, ".alertinner strong")
    MESSAGE_NAME_PRODUCT = (By.CSS_SELECTOR, "#messages .alertinner > strong")
    MESSAGE_BASKET_VALUE = (By.CSS_SELECTOR, "#messages .alertinner p strong")
