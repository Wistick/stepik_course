from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


URL = 'http://suninjuly.github.io/explicit_wait2.html'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    executable_path=' ',
    options=options
)


try:
    driver.implicitly_wait(5)
    driver.get(URL)
    price = WebDriverWait(driver, 12).until(
        ec.text_to_be_present_in_element((By.ID, 'price'), '100')
    )
    driver.find_element_by_css_selector('button[id="book"]').click()
    answer = driver.find_element_by_css_selector('[id="input_value"]').text
    result = calc(answer)
    driver.find_element_by_css_selector('input[id="answer"]').send_keys(result)
    driver.find_element_by_css_selector('button[id="solve"]').click()

    alert = driver.switch_to.alert
    alert_text = alert.text.split()
    alert.accept()
    print(alert_text[-1])
    assert 'Congrats,' == alert_text[0], 'error!'

except Exception as e:
    print(e)
finally:
    driver.close()
    driver.quit()
