import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as OptionsFirefox



def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose a language if you remember its' shortcut")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser_name = request.config.getoption("browser_name")
    if not language:
        raise pytest.UsageError("--language should be set")
    if not browser_name:
        raise pytest.UsageError("--browser_name should be set")
    
    print("\nstart chosen browser for the test..")
    
    if browser_name=="chrome":
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': language})
        browser = webdriver.Chrome(options=options)
        
    elif browser_name=="firefox":
        #deprecated, raises warnings!
        #fp = webdriver.FirefoxProfile()
        #fp.set_preference("intl.accept_languages", language)
        #browser = webdriver.Firefox(firefox_profile=fp)
        
        #updated, looks & works good(aknowlegements -> @Eвгений Мышкин)
        options_firefox = OptionsFirefox()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options_firefox)
    
#pytest -s -v --browser_name=firefox --language=es ~/stepik_adventure1/test_adv1.py    
    yield browser
    print("\nquit browser..")
    browser.quit()