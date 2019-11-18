from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_product_to_cart(self):
        self.browser.find_element(*ProductPageLocators.BUTTON_ADD_TO_CART).click()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def correct_product_name_in_message(self, product_name):
        assert self.browser.find_element(
            *ProductPageLocators.PRODUCT_NAME_IN_MESSAGE).text == product_name, "product name incorrect"


    def correct_price_in_message(self, product_price):
        assert self.browser.find_element(
            *ProductPageLocators.MESSAGE_WITH_PRICE).text == product_price, "product name incorrect"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.MESSAGE_ACCESS_ADD_TO_BASKET), \
            "Success message is presented, but should not be"

    def success_message_is_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.MESSAGE_ACCESS_ADD_TO_BASKET), \
            "Success message is presented, but should not be"
