from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_URL = 'http://selenium1py.pythonanywhere.com/accounts/login/'
    FORM_LOGIN = (By.ID, "login_form")
    FORM_REGISTOR = (By.ID, "register_form")