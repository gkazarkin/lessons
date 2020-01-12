from .basepage import BasePage
from pages.locators import LoginPageLocators
import time
import faker


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        login = "login"
        current_url = self.browser.current_url
        assert login in current_url, f'Expected {login}, but substring is not found at {current_url}'

    @pytest.
    def register_new_user(self, email, password):
        # email = str(time.time()) + "@fakemail.org"
        f = faker.Faker()
        email = f.email()
        # принимает две строки и регистрирует пользователя
        # открыть страницу регистрации
        # зарегистрировать нового пользователя
        # проверить, что пользователь залогинен

    def should_be_login_form(self):
        sign_in_email_field_check = self.is_element_present(*LoginPageLocators.sign_in_email_field)
        # * = Указывает на то, что распокавать кортеж (пару c типом и локатором)
        assert sign_in_email_field_check, "Email field in Sign_in is not presented"

        sign_in_pass_field_check = self.is_element_present(*LoginPageLocators.sign_in_pass_field)
        assert sign_in_pass_field_check, "Login field in Sign_in is not presented"

        sign_in_forgot_pass_link_check = self.is_element_present(*LoginPageLocators.sign_in_forgot_pass_link)
        assert sign_in_forgot_pass_link_check, "Login field in Sign_in is not presented"

        sign_in_btn_check = self.is_element_present(*LoginPageLocators.sign_in_btn)
        assert sign_in_btn_check, "Login field in Sign_in is not presented"
        # assert True

    def should_be_register_form(self):
        reg_email_field_check = self.is_element_present(*LoginPageLocators.reg_email_field)
        assert reg_email_field_check, "Login field in Sign_in is not presented"

        reg_pass_field_check = self.is_element_present(*LoginPageLocators.reg_pass_field)
        assert reg_pass_field_check, "Login field in Sign_in is not presented"

        reg_repeat_pass_field_check = self.is_element_present(*LoginPageLocators.reg_repeat_pass_field)
        assert reg_repeat_pass_field_check, "Login field in Sign_in is not presented"

        reg_btn_check = self.is_element_present(*LoginPageLocators.reg_btn)
        assert reg_btn_check, "Login field in Sign_in is not presented"
        # assert True