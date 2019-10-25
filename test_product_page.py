# Page Object стилизация тест-кейсов для проверки страницы товара

from .pages.product_page import ProductPage


LINK = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'

def test_guest_can_add_product_to_basket(browser):
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    #link = 'http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/'
    link = LINK
    print(link)
    page = ProductPage(browser, link)  # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page.open()  # открываем страницу
    page.should_be_add_product_to_basket()


def test_should_be_cost_of_basket_corresponds_to_price(browser):
    link = LINK
    print(link)
    page = ProductPage(browser, link)
    page.open()
    page.should_be_cost_of_basket_corresponds_to_price()