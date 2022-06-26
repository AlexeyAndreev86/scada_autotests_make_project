# Маппинг отличается от Modbus-TCP в части измерений (регистры 30000)

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pages


def test_modbus_RTU_slave(driver):
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
        
    print(time.asctime(), '\nПараметрируем модуль Modbus RTU (ведомый)')
    time.sleep(0.75)
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Modbus RTU (ведомый)')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Modbus RTU (ведомый)')]").click()
        
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
        print('удаляем все старые каналы Modbus RTU (ведомый)')
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
    COM.send_keys('COM13')
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, '//div[@button_id="tab_devices"]').click()
    time.sleep(0.35)
    driver.find_element(By.XPATH, '//button[text()="Добавить устройство"]').click()
    time.sleep(0.35)
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.5)
    driver.find_element(By.TAG_NAME, "a").click()
    time.sleep(0.4)
    driver.find_element(By.XPATH, '//div[@button_id="tab_mapping"]').click()
    time.sleep(0.4)


    # параметрируем маппинг
    print(time.asctime(), 'Параметрируем маппинг Modbus RTU (ведомый)')
    driver.find_element(By.CSS_SELECTOR, 'div[webix_ai_id="params_tree_acc"]').click()
    # Calculated tags
    driver.find_element(By.XPATH, "//b[text()='CalculatedTags']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='DPI']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='SPI_OFF']/following-sibling::span").click()
    driver.find_element(By.XPATH, "//span[text()='SPI_ON']/following-sibling::span").click()

    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Описание"]').send_keys('SPI_OFF')
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Бит / Длина"]').send_keys('11')

    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Описание"]').send_keys('SPI_ON')
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Бит / Длина"]').send_keys('12' + Keys.ENTER)
    time.sleep(0.3)

    driver.find_element(By.XPATH, "//b[text()='DPI']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Float']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//span[text()='Float']/following-sibling::span[2]").click()
    time.sleep(0.25)
    driver.find_element(By.XPATH, "//span[text()='Float2']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Float4']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Float8']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Float16']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Float32']/following-sibling::span[2]").click()
    time.sleep(0.25)

    for i in range(6):
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(3+i)+'" and @aria-colindex="3"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(3+i)+'" and @aria-colindex="3"]').click()
        driver.find_element(By.XPATH, '//input[@aria-label="Регистр"]').send_keys(str(30000+2*i))
        time.sleep(0.3)
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(3+i)+'" and @aria-colindex="6"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(3+i)+'" and @aria-colindex="6"]').click()
        driver.find_element(By.CSS_SELECTOR, 'option[value="Single"]').click()
        time.sleep(0.25)

    driver.find_element(By.XPATH, "//b[text()='CalculatedTags']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='DatabaseTags']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Group']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='Test']/following-sibling::span[2]").click()
    time.sleep(0.2)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="9" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="9" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Регистр"]').send_keys('30012')
    time.sleep(0.25)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="9" and @aria-colindex="6"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="9" and @aria-colindex="6"]').click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="Single"]').click()
    time.sleep(0.25)

    # Virtual Device 1
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//b[text()='DatabaseTags']").click()
    time.sleep(0.3)

    VIRT = driver.find_element(By.XPATH, "//b[text()='VirtualDevices']")
    time.sleep(0.3)
    driver.execute_script("return arguments[0].scrollIntoView(true);", VIRT)
    time.sleep(0.2)
    VIRT.click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//b[text()='Имитатор']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Device1']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Commands']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//span[text()='Mu_OFF']/following-sibling::span[2]").click()
    time.sleep(0.2)
    driver.find_element(By.XPATH, "//span[text()='Mu_ON']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='SW_BLOCK']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='SW_OFF']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='SW_ON']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='SW_UNBLOCK']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Test_OFF']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Test_ON']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Work_OFF']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Work_ON']/following-sibling::span[2]").click()
    time.sleep(0.2)

    for i in range(10):    
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(10+i)+'" and @aria-colindex="3"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(10+i)+'" and @aria-colindex="3"]').click()
        driver.find_element(By.XPATH, '//input[@aria-label="Регистр"]').send_keys('10000')
        time.sleep(0.3)
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(10+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(10+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//input[@aria-label="Бит / Длина"]').send_keys(str(i))
        time.sleep(0.3)
        
    driver.find_element(By.XPATH, "//b[text()='Commands']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Parameter']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//span[text()='BLOCKED']/following-sibling::span[2]").click()
    time.sleep(0.25)
    driver.find_element(By.XPATH, "//span[text()='Mu']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='RPO']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='RPV']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Test']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='TS1']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='TS2']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='TS3']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='TS4']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='TS5']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Work']/following-sibling::span[2]").click()
    time.sleep(0.25)

    for i in range(1, 11):    
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(20+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(20+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//input[@aria-label="Бит / Длина"]').send_keys(str(i) + Keys.ENTER)
        time.sleep(0.3)

    from project_save import project_save
    project_save(driver)

    print(time.asctime(), 'test_0012 Modbus RTU (ведомый) пройден')
