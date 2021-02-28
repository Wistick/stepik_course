import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default='en',
        help='Choose language: ru, es ... (etc.)'
    )


@pytest.fixture(scope='function')
# browser = driver
def driver(request):
    user_language = request.config.getoption('language')
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    print('\nStarting browser for test...')
    driver = webdriver.Chrome(options=options)
    yield driver
    print('\nQuit browser...')
    driver.quit()
