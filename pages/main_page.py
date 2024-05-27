"""module to test base_page.py"""
from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    """general page for tests"""
    def go_to_login_page(self):
        """open login page"""
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        """check login link"""
        assert self.is_element_present(By.CSS_SELECTOR, "#login_link_invalid"), "Login link is not presented"