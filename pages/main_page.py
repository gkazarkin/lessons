import pytest
import conftest
from selenium.webdriver.common.by import By
from pages.base import Base
from pages.locators import MainPageLocators
from pages.login_page import LoginPage


class MainPage(Base):
    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        # * = Указывает на то, что распокавать кортеж (пару c типом и локатором)
        link.click()
        alert = self.browser.switch_to.alert
        alert.accept()

    def should_be_login_link(self):
        link_check = self.is_element_present(*MainPageLocators.LOGIN_LINK)
        assert link_check, "Login link is not presented"


