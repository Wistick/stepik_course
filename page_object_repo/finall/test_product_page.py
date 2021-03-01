from .pages.product_page import ProductPage


def test_guest_can_add_item_to_basket(driver):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(driver, link)
    page.open()
    page.should_be_product_page()
    page.client_add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_correct_message_alert()
