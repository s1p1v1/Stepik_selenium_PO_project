import time
from .base_page import BasePage
from .locators import LoginPageLocators

class LoginPage(BasePage):
    def register_new_user(self, email, password):
        # Регистрация гостя
        time.sleep(2)
        # заполнение поля ввода адреса email
        input_email = self.browser.find_element(*LoginPageLocators.INPUT_EMAIL)
        input_email.send_keys(email)
        # заполнение поля ввода пароля
        input_password_1 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_1)
        input_password_1.send_keys(password)
        # заполнение поля ввода подтверждения пароля
        input_password_2 = self.browser.find_element(*LoginPageLocators.INPUT_PASSWORD_2)
        input_password_2.send_keys(password)
        # нежатие кнопки регистрации
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        print(self.browser.current_url)
        assert "login" in self.browser.current_url, "Login word in URL is not presented"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"