import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options



# добавляем параметр запуска тестов в командной строке(c  каким языком запускать) По умолчанию не установлен
def pytest_addoption(parser):

    # Можно задать значение параметра по умолчанию,
    # чтобы в командной строке не обязательно было указывать параметр --language
    parser.addoption('--language', action='store', default=None, help="Choose from langs: en/ru/fr/.....")

# Запуск браузера(для каждой функции)
@pytest.fixture(scope="function")  # по умолчанию запускается для каждой функции
def browser(request):
    user_language = request.config.getoption("language")  # получаем параметр командной строки language
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print("\nstart Сhrome browser for test..")
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    browser.quit()