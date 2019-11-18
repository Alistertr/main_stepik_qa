from .base_page import BasePage
from .locators import MainPageLocators, BasketPageLocators


class BasketPage(BasePage):
    def should_be_message_basket_is_empty(self, text_message):
        assert self.browser.find_element(
            *BasketPageLocators.MESSAGE_BASKET_IS_EMPTY).text == text_message, "Message yuor basket is empty NOT FOUND"

    def should_not_be_product_in_basket(self):
        self.is_not_element_present(*BasketPageLocators.PRODUCT_IN_BASKET)

