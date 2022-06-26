from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pages

             
def test_iec104_server(driver):
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
    
    print(time.asctime(), '\nПараметрируем модуль IEC 60870-104 (сервер)')
    time.sleep(0.75)
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'IEC 60870-104 (сервер)')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'IEC 60870-104 (сервер)')]").click()
    
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
        print('удаляем все старые каналы МЭК-104 (сервер)')
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
    
    sinchro = driver.find_element(By.XPATH, '//div[@view_id="$checkbox7"]//button').get_attribute('aria-checked')
    if sinchro == 'true':
        driver.find_element(By.XPATH, '//div[@view_id="$checkbox7"]//button').click()



    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@button_id="tab_sectors"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//button[text()='Добавить сектор']").click()

    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()

    driver.find_element(By.TAG_NAME, 'input').send_keys('3' + Keys.ENTER)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.25)
    driver.find_element(By.TAG_NAME, "a").click()
    time.sleep(0.4)
    driver.find_element(By.XPATH, '//div[@button_id="tab_mapping"]').click()
    time.sleep(0.4)

    # параметрируем маппинг
    print(time.asctime(), 'Параметрируем маппинг МЭК-104 (сервер)')
    driver.find_element(By.CSS_SELECTOR, 'div[webix_ai_id="params_tree_acc"]').click()
    # Calculated tags
    driver.find_element(By.XPATH, "//b[text()='CalculatedTags']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='DPI']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='DPI']/following-sibling::span").click()
    driver.find_element(By.XPATH, "//span[text()='SPI_OFF']/following-sibling::span").click()
    driver.find_element(By.XPATH, "//span[text()='SPI_ON']/following-sibling::span").click()

    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Описание"]').send_keys('DPI' + Keys.ENTER)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Адрес"]').send_keys('20' + Keys.ENTER)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="6"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="6"]').click()
    time.sleep(0.3)
    # символ '\'надо либо экранировать либо делать raw-строку, иначе будет deprication warning
    driver.find_element(By.XPATH, '//div[@view_id="$suggest1"]//div[text()="M_DP_NA_1 \\ DPI"]').click()

    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Описание"]').send_keys('SPI_OFF' + Keys.ENTER)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Адрес"]').send_keys('12' + Keys.ENTER)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="6"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="6"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, r'//div[@view_id="$suggest1"]//div[text()="M_SP_NA_1 \ SPI"]').click()

    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Описание"]').send_keys('SPI_ON' + Keys.ENTER)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Адрес"]').send_keys('13' + Keys.ENTER)
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="6"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="6"]').click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, r'//div[@view_id="$suggest1"]//div[text()="M_SP_NA_1 \ SPI"]').click()

    # Virtual Device 1
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//b[text()='CalculatedTags']").click()
    time.sleep(0.3)

    VIRT = driver.find_element(By.XPATH, "//b[text()='VirtualDevices']")
    time.sleep(0.3)
    driver.execute_script("return arguments[0].scrollIntoView(true);", VIRT)
    time.sleep(0.1)
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
        time.sleep(0.3)
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(4+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(4+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//input[@aria-label="Адрес"]').send_keys(str(50+i))
        time.sleep(0.3)
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(4+i)+'" and @aria-colindex="6"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(4+i)+'" and @aria-colindex="6"]').click()
        time.sleep(0.3)
        driver.find_element(By.XPATH, r'//div[@view_id="$suggest1"]//div[text()="C_SC_NA_1 \ CmdOn"]').click()
        

    driver.find_element(By.XPATH, "//b[text()='Commands']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Parameter']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//span[text()='BLOCKED']/following-sibling::span[2]").click()
    time.sleep(0.2)
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
    time.sleep(0.2)

    for i in range(11):
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(14+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(14+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//input[@aria-label="Адрес"]').send_keys(str(i+1))
        time.sleep(0.3)
    for i in range(11):
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(14+i)+'" and @aria-colindex="6"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(14+i)+'" and @aria-colindex="6"]').click()
        driver.find_element(By.XPATH, r'//div[@view_id="$suggest1"]//div[text()="M_SP_NA_1 \ SPI"]').click()
        time.sleep(0.3)


    # Virtual Device 2
    driver.find_element(By.XPATH, "//b[text()='Device1']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Device2']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//b[text()='Parameter']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//span[text()='F']/following-sibling::span[2]").click()
    time.sleep(0.2)
    driver.find_element(By.XPATH, "//span[text()='Ia']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Ib']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Ic']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Ua']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Ub']/following-sibling::span[2]").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, "//span[text()='Uc']/following-sibling::span[2]").click()
    time.sleep(0.2)


    driver.find_element(By.XPATH, '//div[@aria-rowindex="31" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="31" and @aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//input[@aria-label="Адрес"]').send_keys('106')
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="31" and @aria-colindex="6"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="31" and @aria-colindex="6"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, r'//div[@view_id="$suggest1"]//div[text()="M_ME_NC_1 \ FLOAT"]').click()
    time.sleep(0.1)

    driver.find_element(By.CSS_SELECTOR, 'button[webix_p_id="0"]').click()
    time.sleep(0.5)

    for i in range(6):
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(25+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(25+i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//input[@aria-label="Адрес"]').send_keys(str(100+i))
        time.sleep(0.1)
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(25+i)+'" and @aria-colindex="6"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(25+i)+'" and @aria-colindex="6"]').click()
        time.sleep(0.1)
        driver.find_element(By.XPATH, r'//div[@view_id="$suggest1"]//div[text()="M_ME_NC_1 \ FLOAT"]').click()
        time.sleep(0.1)

    from project_save import project_save
    project_save(driver)
    
    print(time.asctime(), 'test_0008 IEC 60870-104 (сервер) пройден')
