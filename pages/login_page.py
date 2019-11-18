from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        current_url = self.browser.current_url
        assert current_url == LoginPageLocators.LOGIN_URL, "url not correct. Current url{}".format(current_url)

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "form login not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.FORM_LOGIN), "form registr not present"