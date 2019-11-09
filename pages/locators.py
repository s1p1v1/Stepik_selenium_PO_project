# Классы локаторы для Page Object

from selenium.webdriver.common.by import By

class BasePageLocators():
    # селекторы для всех наследущих BasePage классов (PO)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, ".basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class MainPageLocators():
    # каждый селектор — это пара: как искать и что искать
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    #LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")
    pass

class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
    INPUT_EMAIL = (By.ID, 'id_registration-email')
    INPUT_PASSWORD_1 = (By.ID, 'id_registration-password1')
    INPUT_PASSWORD_2 = (By.ID, 'id_registration-password2')
    REGISTER_BUTTON = (By.CSS_SELECTOR, '#register_form .btn')


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
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert")

class BasketPageLocators():
    #BASKET_ITEM = (By.CSS_SELECTOR, ".basket-items")
    BASKET = (By.CSS_SELECTOR, "#basket_formset")
    #BASKET = (By.CSS_SELECTOR, "#content_inner #basket_formset")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#content_inner p")

