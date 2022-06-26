from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pages


def test_virtual_devices(driver):
    page_exchange = pages.page_exchange

    driver.implicitly_wait(10)
    driver.get(page_exchange)
    time.sleep(1)
    title = driver.title
    
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
        driver.get(page_exchange)


    print(time.asctime(), '\nПараметрируем список виртуальных устройств')
    time.sleep(0.75)
    
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Виртуальные устройства')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        # обновляем страницу в случае StaleElementReferenceException (перестраивается DOM-структура страницы)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Виртуальные устройства')]").click()

    driver.switch_to.frame(0)


    autostart = driver.find_element(By.XPATH, '//button[@aria-label="Автозапуск:"]').get_attribute('aria-checked')
    if autostart == 'false':
        driver.find_element(By.XPATH, "//label[text()='Автозапуск:']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(2)

  
    driver.find_element(By.XPATH, "//div[@button_id='tab_groups']").click()
    # проверяем наличие возможных групп в модуле, удаляем при наличие
    groups = driver.find_elements(By.XPATH, '//div[@aria-colindex="3"]')
    if len(groups)>0:
        print('удаляем все группы, входящие в модуль ВИРТУАЛЬНЫЕ УСТРОЙСТВА')
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@title='Удалить все']").click()
        driver.find_element(By.XPATH, "//div[text()='Да']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)


    driver.find_element(By.XPATH, "//button[text()='Добавить группу']").click()
    time.sleep(1)

    new_group_name = driver.find_element(By.XPATH, "//div[@column='1']")
    new_group_name.click()

    action = ActionChains(driver)
    action.double_click(on_element=new_group_name)
    action.perform()

    driver.find_element(By.XPATH, "//input[@aria-label='Группа']").send_keys('Имитатор' + Keys.ENTER)
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(1)

    driver.find_element(By.TAG_NAME, "a").click()

    driver.find_element(By.XPATH, '//div[@button_id="tab_devices"]').click()
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Добавить устройство']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Добавить устройство']").click()
    time.sleep(1)


    device_1 = driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="3"]')
    device_1.click()
    # перестраивается DOM - ищем элемент повторно
    device_11 = driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and @aria-colindex="3"]')
    action = ActionChains(driver)
    action.double_click(on_element=device_11)
    action.perform()
    driver.find_element(By.XPATH, '//div[@webix_l_id="Bdps_TU_TS.xml"]').click()

    time.sleep(1)

    device_2 = driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="3"]')
    device_2.click()
    device_12 = driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="3"]')
    action = ActionChains(driver)
    action.double_click(on_element=device_12)
    action.perform()
    driver.find_element(By.XPATH, '//div[@webix_l_id="Электрогенератор_100V_5A.xml"]').click()

    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(1)
    driver.switch_to.parent_frame()

    imitator = driver.find_element(By.XPATH, "//span[text()='Имитатор']//preceding-sibling::div[contains(@class, 'webix_tree_plus2')]")
    driver.execute_script("arguments[0].scrollIntoView();", imitator)
    imitator.click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//span[text()='Device1 (Bdps_TU_TS.xml)']").click()
    driver.switch_to.frame(0)
    driver.find_element(By.XPATH, '//label[text()="Период, мс:"]/following-sibling::input').clear()
    driver.find_element(By.XPATH, '//label[text()="Период, мс:"]/following-sibling::input').send_keys('1000')
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()

    time.sleep(1)
    driver.switch_to.parent_frame()
    driver.find_element(By.XPATH, "//span[text()='Device2 (Электрогенератор_100V_5A.xml)']").click()
    driver.switch_to.frame(0)
    driver.find_element(By.XPATH, '//label[text()="Период, мс:"]/following-sibling::input').clear()
    driver.find_element(By.XPATH, '//label[text()="Период, мс:"]/following-sibling::input').send_keys('1000')
    
    from project_save import project_save
    project_save(driver)
    
    print(time.asctime(), 'test_0004_exchange_virtual_devices пройден')
