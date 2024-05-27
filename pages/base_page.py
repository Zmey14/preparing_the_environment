"""base module for all pages"""
from selenium.common.exceptions import NoSuchElementException

class BasePage():
    """base class for all pages"""
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        """open page"""
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        """check is element present"""
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True