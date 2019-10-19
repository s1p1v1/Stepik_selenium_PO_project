# Базовый Page Object, содержащий вспомогательные методы работы с драйвером

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)

