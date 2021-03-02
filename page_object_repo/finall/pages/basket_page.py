from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_basket_page(self):
        self.should_be_basket_url()

    def should_be_empty_basket(self):
        self.should_be_message_empty_basket()
        self.should_be_no_item_in_basket()

    def should_be_basket_url(self):
        assert 'basket' in self.driver.current_url, 'Wrong URL page! Should end on "/basket/"!'

    def should_be_message_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), 'Another message is presented, ' \
                                                                              'but should not be'

    def should_be_no_item_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_HAS_ITEM_AVAILABILITY), 'Item in basket is ' \
                                                                                              'presented, but should ' \
                                                                                              'not be'
