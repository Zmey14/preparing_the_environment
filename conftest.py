from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest



def pytest_addoption(parser):
    parser.addoption("--language", action="store", default="en",
                     help="input language")



@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    print("\nstart browser..")
    web_browser = webdriver.Chrome(options=options)
    yield web_browser
    print("\nquit browser..")
    web_browser.quit()