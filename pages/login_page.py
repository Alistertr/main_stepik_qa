from .base_page import BasePage
from .locators import LoginPageLocators

LOGIN_URL = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == LOGIN_URL, "url not correct. Current url {}".format(current_url)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "form login not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "form registr not present"

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.FIELD_MAIL_FOR_REGISTRATION).send_keys(email)
        self.browser.find_element(*LoginPageLocators.FIELD_PASS_FOR_REGISTRATION).send_keys(password)
        self.browser.find_element(*LoginPageLocators.FIELD_CONFIRM_PASS).send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_SIGNUP).click()


