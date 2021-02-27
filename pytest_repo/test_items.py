import time

URL = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'


def test_check_basket_button(driver):
    driver.get(URL)
    # time.sleep(30)
    button = len(driver.find_elements_by_css_selector('.btn.btn-lg.btn-primary'))
    assert button > 0, 'Error! Element does not exist!'
