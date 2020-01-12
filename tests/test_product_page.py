from pages.locators import ProductPageLocator
from pages.product_page import ProductPage
import pytest


def test_guest_can_add_product_to_basket(browser):
    page = ProductPage(browser, ProductPageLocator.link)
    page.open()
    page.should_be_product_page()
