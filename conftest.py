import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser', action='store', default='chrome')
    parser.addoption('--ui', action='store', default='yes')


@pytest.fixture(scope='session')
def driver(request):
    browser = request.config.getoption('browser')
    ui = request.config.getoption('ui')
    if browser == 'chrome':
        options = webdriver.ChromeOptions()
        options.add_argument('--log-level=3')
        options.add_argument('--start-maximized')
        
        if ui == 'no':
            options.add_argument('--headless')

        print('\nАвтотесты будут выполнены в браузере Chrome')
        driver = webdriver.Chrome(options=options)
        if ui == 'no':
            driver.set_window_size(1920, 1080)
            
    elif browser == 'firefox':
        options = webdriver.FirefoxOptions()
        if ui == 'no':
            options.headless=True

        print('\nАвтотесты будут выполнены в браузере Mozilla')
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
    else:
        raise pytest.UsageError('Введите chrome или firefox')
    yield driver
    print('Закрываем браузер')
    driver.quit()
    
