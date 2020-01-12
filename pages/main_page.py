import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from pages.locators import MainPageLocators


class MainPage(BasePage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()

    def should_be_login_link(self):
        wrong_login = self.is_element_present(*MainPageLocators.LOGIN_LINK)  # * = Указывает на то, что распокавать кортеж (пару)
        assert wrong_login, "Login link is not presented"


