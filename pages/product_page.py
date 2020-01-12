import time
from pages.locators import ProductPageLocator
from pages.basepage import BasePage


class ProductPage(BasePage):
    def should_be_product_page(self):
        self.should_be_login_url()
        self.should_be_add_to_cart_button()
        self.add_product_to_cart()
        self.should_be_success_message()
        self.check_price_added()

    def should_be_login_url(self):
        promo = "promo="
        current_url = self.browser.current_url
        assert promo in current_url, f'Expected {promo}, but substring is not found at {current_url}'

    def should_be_add_to_cart_button(self):
        shop_cart_check = self.is_element_present(*ProductPageLocator.shop_cart)
        # * = Указывает на то, что распокавать кортеж (пару c типом и локатором)
        assert shop_cart_check, "Shop cart button is not presented"

    def add_product_to_cart(self):
        cart = self.browser.find_element(*ProductPageLocator.shop_cart)
        cart.click()

    def should_be_success_message(self):
        self.solve_quiz_and_get_code()

    def check_price_added(self):
        book_name = self.browser.find_element(*ProductPageLocator.book_name_loc).text
        print(book_name)
        # price_green = self.browser.find_element(*ProductPageLocator.price_green_loc).text
        # basket_price = self.browser.find_element(*ProductPageLocator.basket_price_loc).text
        # assert price_green == basket_price, "Price in basket is not equal"

    # def should_not_be_success_message(self):
    #     assert self.is_not_element_present(*ProductPageLocator.SUCCESS_MESSAGE), \
    #         "Success message is presented, but should not be"

    # def should_not_be_success_message(self):
    #     assert self.is_disappeared(*ProductPageLocator.SUCCESS_MESSAGE2), \
    #         "Success message is presented, but should not be"


