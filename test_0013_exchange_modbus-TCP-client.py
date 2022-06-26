from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pages


def test_modbus_TCP_client(driver):
    page_exchange = pages.page_exchange

    driver.implicitly_wait(3)
    driver.get(page_exchange)
    time.sleep(1)
    title = driver.title
        
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
        time.sleep(1)
        driver.get(page_exchange)
        
    print(time.asctime(), '\nПараметрируем модуль Modbus TCP (клиент)')
    time.sleep(0.75)

    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Modbus TCP (клиент)')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Modbus TCP (клиент)')]").click()

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
        print('удаляем все старые каналы Modbus TCP (клиент)')
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

    time.sleep(0.2)
    TIMEOUT_READ = driver.find_element(By.XPATH, '//label[text()="Таймаут(чтение), мс:"]/following-sibling::input')
    TIMEOUT_READ.clear()
    TIMEOUT_READ.send_keys('700')
    time.sleep(0.2)
    TIMEOUT_WRITE = driver.find_element(By.XPATH, '//label[text()="Таймаут(запись), мс:"]/following-sibling::input')
    TIMEOUT_WRITE.clear()
    TIMEOUT_WRITE.send_keys('500')
    time.sleep(0.2)
    TIMEOUT = driver.find_element(By.XPATH, '//label[text()="Таймаут(между запросами), мс:"]/following-sibling::input')
    TIMEOUT.clear()
    TIMEOUT.send_keys('100')
    REPEAT = driver.find_element(By.CSS_SELECTOR, 'div[view_id="$text10"] input')
    REPEAT.clear()
    REPEAT.send_keys('2')
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, '//div[@button_id="tab_devices"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//button[text()="Добавить устройство"]').click()
    time.sleep(0.25)

    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@webix_l_id="Modbus.xml"]').click()
    time.sleep(0.25)
    
    from project_save import project_save
    project_save(driver)

    print(time.asctime(), 'test_0013 IModbus TCP (клиент) пройден')
