# Page Object главной страницы приложения

from .base_page import BasePage
#from selenium.webdriver.common.by import By
#from .locators import MainPageLocators
#from .login_page import LoginPage

class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
    '''
    #   вынесено в класс BasePage  
    def go_to_login_page(self):
        #login_link = self.browser.find_element(By.CSS_SELECTOR, "#registration_link")
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        #return LoginPage(self.browser, self.browser.current_url) # реализация перехода в самом MainPage

    def should_be_login_link(self):
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"
        #assert self.is_element_present(By.CSS_SELECTOR, "#login_link"), "Login link is not presented"
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
    '''