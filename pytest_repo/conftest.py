import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        '--language',
        action='store',
        default=None,
        help='Choose language: ru, es ... (etc.)'
    )


@pytest.fixture(scope='function')
def browser(request):
    user_language = request.config.getoption('language')
    options = webdriver.ChromeOptions()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language}
    )
    print('\nStarting browser for test...')
    browser = webdriver.Chrome(options=options)
    yield browser
    print('\nQuit browser...')
    browser.quit()
