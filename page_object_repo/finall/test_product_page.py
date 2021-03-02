import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage


def test_guest_can_add_item_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_product_page()
    page.client_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_message_alert()


def test_guest_should_see_login_link_on_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_login_link()


def test_guest_can_go_to_login_page_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = ProductPage(driver, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(driver, driver.current_url)
    basket_page.should_be_basket_url()
    basket_page.should_be_empty_basket()


xfile = 7
mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
URLS = [mask+str(i) for i in range(10) if i != xfile]
xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
URLS.insert(xfile, xlink)


@pytest.mark.parametrize('url', URLS)
def test_guest_can_add_item_to_basket_promo(driver, url):
    page = ProductPage(driver, url)
    page.open()
    page.should_be_product_page()
    page.client_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_message_alert()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(driver, link)
    page.open()
    page.client_add_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(driver, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/hacking-exposed-wireless_208/'
    page = ProductPage(driver, link)
    page.open()
    page.client_add_to_basket()
    page.should_be_disappeared_element()
