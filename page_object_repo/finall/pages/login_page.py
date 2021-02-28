from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert 'login' in self.driver.current_url, 'Wrong URL page! Should end on "/login/"!'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), 'Login Email input field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), 'Login password input field is not presented'
        assert self.is_element_present(*LoginPageLocators.LOGIN_BUTTON), 'Login button is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REG_EMAIL), 'Registration Email input filed is not presented'
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD), 'Registration password input filed is not ' \
                                                                         'presented'
        assert self.is_element_present(*LoginPageLocators.REG_PASSWORD_CONF), 'Registration confirm password input ' \
                                                                              'filed is not presented'
        assert self.is_element_present(*LoginPageLocators.REG_BUTTON), 'Registration button is not presented'
