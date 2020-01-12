import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
# import time
# import math
import conftest
from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.locators import MainPageLocators
from pages.locators import LoginPageLocators

@pytest.mark.login_guest
class TestLoginFromMainPage():
    # не забываем передать первым аргументом self
    def test_guest_can_go_to_login_page(self, browser):
        pass

    def test_guest_should_see_login_link(self, browser):
        pass

    def test_guest_can_go_to_login_page(browser):
        # link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, MainPageLocators.link)  # передаем в конструктор экземпляр драйвера и url адрес
        page.open()
        # page.should_be_login_link()
        # page.go_to_login_page()
        # login_page = LoginPage(browser, browser.current_url)
        # login_page.should_be_login_page()

    def test_guest_should_see_login_link(browser):
        # link = "http://selenium1py.pythonanywhere.com/"
        page = MainPage(browser, MainPageLocators.link)
        page.open()
        page.go_to_login_page()
        page.should_be_login_link()

    def test_login_url(browser):
        page = LoginPage(browser, LoginPageLocators.url_login)
        page.open()
        page.should_be_login_page()

    def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
        pass
        # Гость открывает главную страницу
        # Переходит в корзину по кнопке в шапке сайта
        # Ожидаем, что в корзине нет товаров
        # Ожидаем, что есть текст о том что корзина пуста

    # def test_add_to_cart(browser):
    #     page = ProductPage(url="", browser)   # инициализируем объект Page Object
    #     page.open()                           # открываем страницу в браузере
    #     page.should_be_add_to_cart_button()   # проверяем что есть кнопка добавления в корзину
    #     page.add_product_to_cart()            # жмем кнопку добавить в корзину
    #     page.should_be_success_message()      # проверяем что есть сообщение с нужным текстом
