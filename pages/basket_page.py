from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_success_product(self):
        # проверка отсутствия продуктов в корзине
        assert self.is_not_element_present(*BasketPageLocators.BASKET), "Basket is empty"

    def should_is_cart_message_present(self):
        # проверка наличия сообщения о пустой корзине
        message = self.browser.find_element(*BasketPageLocators.SUCCESS_MESSAGE)
        #print('message:', message.text)
        assert self.is_element_present(*BasketPageLocators.SUCCESS_MESSAGE), "Missing message about an empty cart"

