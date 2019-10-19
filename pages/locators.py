# Классы локаторы для Page Object

from selenium.webdriver.common.by import By

class MainPageLocators():
    # каждый селектор — это пара: как искать и что искать
    #LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators():
    LOGIN_FORM = (By.ID, 'login_form')
    REGISTER_FORM = (By.ID, 'register_form')
