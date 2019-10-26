import time
from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        #print(*ProductPageLocators.PRODUCT_BUTTON)
        button = self.browser.find_element(*ProductPageLocators.PRODUCT_BUTTON)
        button.click()
        time.sleep(2)
        self.solve_quiz_and_get_code()

    def should_be_add_product_to_basket(self):
        # реализуйте проверку, что название товара в сообщении соответствует добавляемому товару
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        print('name page:', name_product.text)
        self.add_product_to_basket()
        time.sleep(10)   # без ожидания не успевает появиться сообщение?
        basket_name_product = self.browser.find_element(*ProductPageLocators.MESSAGE_NAME_PRODUCT)
        print('name basket:', basket_name_product.text)
        assert name_product.text == basket_name_product.text, \
            'The product name in the price does not match the product name in the message'

    def should_be_cost_of_basket_corresponds_to_price(self):
        # реализуйте проверку, что стоимость корзины совпадает с ценой товара
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        print('price page:', price_product.text)
        self.add_product_to_basket()
        time.sleep(10)  # без ожидания не успевает появиться сообщение?
        basket_value_product = self.browser.find_element(*ProductPageLocators.MESSAGE_BASKET_VALUE)
        print('value basket:', basket_value_product.text)
        assert price_product.text == basket_value_product.text, \
            'The price of the item does not match the value of the item in the cart'

    def should_not_be_success_message(self):
        # проверка отсутствия элемента в течение заданного времени
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_is_disappeared(self):
        # проверка отсутствия элемента после заданного времени
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "The success message is present, although it should disappear"

