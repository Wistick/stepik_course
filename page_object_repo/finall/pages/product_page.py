from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def go_to_basket_page(self):
        link = self.driver.find_element(*ProductPageLocators.BASKET_BUTTON)
        link.click()

    def client_add_to_basket(self):
        link = self.driver.find_element(*ProductPageLocators.BASKET_BUTTON_ADD)
        link.click()

    def should_be_product_page(self):
        self.should_be_catalogue_url()
        self.should_be_basket_button()

    def should_be_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_BUTTON_ADD), 'Basket button is not presented'

    def should_be_catalogue_url(self):
        assert 'catalogue' in self.driver.current_url, 'Wrong URL Should be catalogue page'
        # assert '?promo=offer' in self.driver.current_url, 'Wrong URL! Should be promo page'
        # assert '?promo=newYear' in self.driver.current_url, 'Wrong URL! Should be promo page'

    def should_be_correct_message_alert(self):
        assert self.is_element_present(*ProductPageLocators.ITEM_NAME), 'Item name is not presented'
        assert self.is_element_present(*ProductPageLocators.ITEM_PRICE), 'Item price is not presented'

        item_name = self.driver.find_element(*ProductPageLocators.ITEM_NAME).text
        item_price = self.driver.find_element(*ProductPageLocators.ITEM_PRICE).text

        assert self.is_element_present(*ProductPageLocators.BASKET_NAME), 'Basket item name is not presented'
        assert self.is_element_present(*ProductPageLocators.BASKET_PRICE), 'Basket item price is not presented'

        basket_name = self.driver.find_element(*ProductPageLocators.BASKET_NAME).text
        basket_price = self.driver.find_element(*ProductPageLocators.BASKET_PRICE).text

        print(f'\nItem name {item_name} = {basket_name}\nItem price {item_price} = {basket_price}\n')

        assert item_name == basket_name, 'Item name does not match!'
        assert item_price == basket_price, 'Item price does not match!'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.BASKET_NAME), 'Success message is presented, ' \
                                                                              'but should not be'

    def should_be_disappeared_element(self):
        assert self.is_disappeared(*ProductPageLocators.BASKET_NAME), 'Success message is presented, but should not be'
