import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru', help="Select language")

@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption('language')   # В переменную user_language передается параметр из командной строки
    options = Options()  # Инициализируются опции браузера
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})  # В опции вебдрайвера передаем параметр из командной строки

    print("\nstart browser for test..")
    browser = webdriver.Chrome(options=options)

    browser.implicitly_wait(5)
    yield browser
    print("\nquit browser..")
    browser.quit()
