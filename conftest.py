import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    #parser.addoption('--browser_name', action='store', default=None, help="Choose browser: chrome or firefox")
    parser.addoption('--browser_name', action='store', default="firefox", help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en', help="Choose language: ru, en, es, fr")

@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    print(browser_name, user_language)
    browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test...")
        # 071019
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
        # browser = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        # 071019
        fp = webdriver.FirefoxProfile()
        fp.set_preference("intl.accept_languages", user_language)
        browser = webdriver.Firefox(firefox_profile=fp)
        #browser = webdriver.Firefox()
    else:
        # raise pytest.UsageError("--browser_name should be chrome or firefox")
        raise pytest.UsageError("specify the parameters: --browser_name, --language")
    yield browser
    print("\nquit browser...")
    browser.quit()
