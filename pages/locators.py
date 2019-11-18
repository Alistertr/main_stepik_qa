from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/en-gb/accounts/login/'
    FORM_LOGIN = (By.ID, "login_form")
    FORM_REGISTOR = (By.ID, "register_form")


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