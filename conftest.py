"""
Метод pytest_addoption парсит команду и получается из нее переменную language,
которую передает в фиксутру browser, которая инциализирует драйвер браузера Chrome
а так же изменяет языковую настройку браузера на основе полученных данных из переменной
language
"""
from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption("--language", action='store', default=None,
                     help="Chose language")

@pytest.fixture(scope='function')
def browser(request):
    language = request.config.getoption("language")
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    print("\nstart browser")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nstop browser")
    browser.quit()

