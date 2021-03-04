from selenium import webdriver


options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    options=options
    )

try:
    url = 'http://suninjuly.github.io/registration2.html'
    driver.get(url)
    driver.find_element_by_css_selector('.first_block > .form-group.first_class > input').send_keys('Name')
    driver.find_element_by_css_selector('.first_block > .form-group.second_class > input').send_keys('Last name')
    driver.find_element_by_css_selector('.first_block > .form-group.third_class > input').send_keys('email')
    driver.find_element_by_css_selector('.second_block > .form-group.first_class > input').send_keys('77777777')
    driver.find_element_by_css_selector('.second_block > .form-group.second_class > input').send_keys('address')
    driver.find_element_by_css_selector('button[type="submit"]').click()

    congratz = driver.find_element_by_css_selector('h1').text
    assert 'Congratulations! You have successfully registered!' == congratz

except Exception as e:
    print(e)
finally:
    driver.quit()
