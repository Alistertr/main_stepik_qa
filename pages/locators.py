from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BUTTON_SEE_BASKET = (By.CSS_SELECTOR, ".btn-group > .btn:first-child")



class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    FORM_LOGIN = (By.ID, "login_form")
    FORM_REGISTOR = (By.ID, "register_form")
    FIELD_MAIL_FOR_REGISTRATION = (By.NAME, "registration-email")
    FIELD_PASS_FOR_REGISTRATION = (By.NAME, "registration-password1")
    FIELD_CONFIRM_PASS = (By.NAME, "registration-password2")
    BUTTON_SIGNUP = (By.NAME, "registration_submit")


class ProductPageLocators():
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    BUTTON_ADD_TO_CART = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.XPATH, '//div[@class="col-sm-6 product_main"]/h1')
    PRODUCT_NAME_IN_MESSAGE = (By.XPATH, "(//div[@class='alertinner '])[1]/strong")
    MESSAGE_WITH_PRICE = (By.XPATH, "(//div[@class='alertinner '])[3]/p/strong")
    MESSAGE_ACCESS_ADD_TO_BASKET = (By.XPATH, "(//div[@class='alertinner '])[1]")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    TEXT_MESSAGE_IS_EMPTY = 'Ваша корзина пуста Продолжить покупки'
    MESSAGE_BASKET_IS_EMPTY = (By.ID, "content_inner")
    PRODUCT_IN_BASKET = (By.CSS_SELECTOR, ".basket-items")