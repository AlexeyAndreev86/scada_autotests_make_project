from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pages


def test_start_exchange(driver):     
    page_exchange = pages.page_exchange

    driver.implicitly_wait(3)
    driver.get(page_exchange)
    time.sleep(1)
    title = driver.title
        
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
        driver.get(page_exchange)
        time.sleep(1)

    print(time.asctime(), '\nЗапускаем сервера опроса')
    time.sleep(0.75)

    try:
        driver.find_element(By.XPATH, '//span[text()="Сервер опроса"]').click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, '//span[text()="Сервер опроса"]').click()

    driver.switch_to.frame(0)
    time.sleep(1)

    autostart = driver.find_element(By.XPATH, '//button[@aria-label="Автозапуск:"]').get_attribute('aria-checked')
    if autostart == 'false':
        driver.find_element(By.XPATH, "//label[text()='Автозапуск:']").click()
        from project_save import project_save
        project_save(driver)
    else:
        driver.switch_to.parent_frame()

    server_start = driver.find_elements(By.XPATH,'//span[text()="Сервер опроса"]/preceding-sibling::div[@class="webix_tree_file control state_stopped"]')
    if len(server_start) == 1:
        server_start = server_start[0]
        server_start.click()

    time.sleep(5)
    working_modules = driver.find_elements(By.CSS_SELECTOR, '.webix_tree_file.control.state_started')
    assert len(working_modules) == 14, "Стартанули не все модули"
        
    print(time.asctime(), 'test_0015_exchange_start пройден')
