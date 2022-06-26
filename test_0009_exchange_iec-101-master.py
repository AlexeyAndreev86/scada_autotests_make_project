from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pages


def test_iec101_master(driver):        
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
        
    print(time.asctime(), '\nПараметрируем модуль IEC 60870-101 (ведущий)')
    time.sleep(0.75)
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'IEC 60870-101 (ведущий)')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'IEC 60870-101 (ведущий)')]").click()

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
        print('удаляем все старые каналы МЭК-101 (ведущий)')
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

    COM = driver.find_element(By.XPATH, '//label[text()="Канал:"]/following-sibling::input')
    COM.clear()
    COM.send_keys('COM14')

    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@view_id="$select3"]//select').click()
    driver.find_element(By.XPATH, '//div[@view_id="$select3"]//option[@value="2"]').click()

    time.sleep(0.25)
    TIMEOUT = driver.find_element(By.XPATH, '//label[text()="Таймаут(между запросами), мс:"]/following-sibling::input')
    TIMEOUT.clear()
    TIMEOUT.send_keys('200')

    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, '//div[@button_id="tab_devices"]').click()
    time.sleep(0.35)
    driver.find_element(By.XPATH, '//button[text()="Добавить устройство"]').click()
    time.sleep(0.35)

    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()
    time.sleep(0.25)
    driver.find_element(By.TAG_NAME, "input").send_keys('3')
    time.sleep(0.25)

    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@webix_l_id="МЭК-101 v1.xml"]').click()
    time.sleep(0.25)
    
    from project_save import project_save
    project_save(driver)

    print(time.asctime(), 'test_0009 IEC 60870-101 (ведущий) пройден')
