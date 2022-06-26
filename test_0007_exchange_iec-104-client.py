from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pages


def test_iec104_client(driver):
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
    
    print(time.asctime(), '\nПараметрируем модуль IEC 60870-104 (клиент)')
    time.sleep(0.75)

    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'IEC 60870-104 (клиент)')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        # обновляем страницу в случае StaleElementReferenceException (перестраивается DOM-структура страницы)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'IEC 60870-104 (клиент)')]").click()

    driver.switch_to.frame(0)

    autostart = driver.find_element(By.XPATH, '//button[@aria-label="Автозапуск:"]').get_attribute('aria-checked')
    if autostart == 'false':
        driver.find_element(By.XPATH, "//label[text()='Автозапуск:']").click()

    debug = driver.find_element(By.XPATH, '//button[@aria-label="Режим отладки:"]').get_attribute('aria-checked')
    if debug == 'false':
        driver.find_element(By.XPATH, "//label[text()='Режим отладки:']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)

    driver.find_element(By.XPATH, "//div[@button_id='tab_channels']").click()
    chanels = driver.find_elements(By.XPATH, '//div[@aria-colindex="3"]')
    if len(chanels)>0:
        print('удаляем все старые каналы МЭК-104 (клиент)')
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@title='Удалить все']").click()
        driver.find_element(By.XPATH, "//div[text()='Да']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Добавить канал']").click()
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.5)
    driver.find_element(By.TAG_NAME, "a").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@button_id="tab_devices"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@view_id="dev_name"]').click()
    time.sleep(0.5)
    file = driver.find_element(By.XPATH, '//div[@view_id="$suggest7_list"]//div[@webix_l_id="МЭК-104 v1.xml"]')
    file.click()
    
    from project_save import project_save
    project_save(driver)
    
    print(time.asctime(), 'test_0007 IEC 60870-104 (клиент) пройден')
