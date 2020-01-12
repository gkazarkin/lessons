from selenium.webdriver.common.by import By


class MainPageLocators():
    link = "http://selenium1py.pythonanywhere.com/"
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    url_login = "http://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
    sign_in_email_field = (By.CSS_SELECTOR, "#id_login-username")
    sign_in_pass_field = (By.CSS_SELECTOR, "#id_login-password")
    sign_in_forgot_pass_link = (By.LINK_TEXT, "I've forgotten my password")
    sign_in_btn = (By.NAME, "login_submit")

    reg_email_field = (By.CSS_SELECTOR, "#id_registration-email")
    reg_pass_field = (By.CSS_SELECTOR, "#id_registration-password1")
    reg_repeat_pass_field = (By.CSS_SELECTOR, "#id_registration-password2")
    reg_btn = (By.NAME, "registration_submit")


class ProductPageLocator():
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    shop_cart = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    price_green_loc = (By.CLASS_NAME, "price_color")
    basket_price_loc = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/text()')
    book_name_loc = (By.CSS_SELECTOR, '[class="col-sm-6 product_main"] h1')
