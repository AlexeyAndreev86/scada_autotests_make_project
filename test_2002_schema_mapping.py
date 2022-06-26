from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.action_chains import ActionChains
import pages


def test_scheme_mapping(driver):
    page_schemas = pages.page_schemas

    driver.implicitly_wait(3)
    driver.get(page_schemas)
    time.sleep(1)
    title = driver.title
    
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
        driver.get(page_schemas)
        time.sleep(1)

    print(time.asctime(), 'делаем привязки сигналов к элементам мнемосхемы')

    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, '.wxi-pencil').click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geSprite.geSprite-link')))

    cfg_btn = driver.find_element(By.CSS_SELECTOR, ".geSprite.geSprite-link")

    # Modbus RTU
    a_1 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='2386']")
    action = ActionChains(driver)
    action.double_click(on_element = a_1)
    action.perform()

    cfg_btn.click()
    driver.find_element(By.XPATH, '//b[text()="Modbus RTU"]//parent::span//preceding-sibling::div[@class="webix_tree_close"]').click()

    action = ActionChains(driver)
    src = driver.find_element(By.XPATH, '//b[text()="Выключатель"]')
    target = driver.find_element(By.XPATH, '//div[text()="Состояние:"]//parent::div//following-sibling::div//input')
    action.drag_and_drop(src, target)
    action.perform()

    cmd = driver.find_element(By.XPATH, '//div[text()="Команды:"]')
    scrl = driver.find_element(By.XPATH, '//div[text()="Цвет заливки:"]')
    driver.execute_script("arguments[0].scrollIntoView();", cmd)
    cmd.click()
    driver.execute_script("arguments[0].scrollIntoView();", scrl)

    driver.find_element(By.XPATH, '//b[text()="Modbus RTU"]/ancestor::div[@class="webix_tree_branch_2"]//b[text()="Выключатель"]/ancestor::span/preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//b[text()="Выключатель"]//ancestor::div[@class="webix_tree_branch_3"]//span[text()="Команды"]//preceding-sibling::div[@class="webix_tree_close"]').click()

    down = driver.find_element(By.XPATH, '//span[text()="Блокировка"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    commands = driver.find_elements(By.XPATH, '//span[text()="Команды"]/ancestor::div[@class="webix_tree_branch_4"]//div[@class="webix_tree_branch_5"]')
    for i in commands:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.XPATH, '//div[@role="tabpanel"]//div[@role="listbox"]')
        action.drag_and_drop(src, target)
        action.perform()

    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, '.webix_tree_branch_3 .webix_tree_open').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()
    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, '.tbl4').click()

    cfg_btn.click()

    driver.find_element(By.XPATH, '//b[text()="Измерения"]//ancestor::span//preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//span[text()="Оперативная информация"]/preceding-sibling::div[@class="webix_tree_close"]').click()

    down = driver.find_element(By.XPATH, '//b[text()="Modbus TCP"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    measures = driver.find_elements(By.CSS_SELECTOR, '.webix_tree_branch_5')
    for i in measures:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.CSS_SELECTOR, '.webix_accordionitem_body .webix_view.webix_list')
        action.drag_and_drop(src, target)
        action.perform()
        
    driver.find_element(By.XPATH, '//b[text()="Modbus RTU"]/ancestor::div[@role="treeitem"]/div[@class="webix_tree_open"]').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()

    # Modbus TCP


    a_4 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='2762.5']")
    action = ActionChains(driver)
    action.double_click(on_element = a_4)
    action.perform()


    cfg_btn.click()
    driver.find_element(By.XPATH, '//b[text()="Modbus TCP"]//parent::span//preceding-sibling::div[@class="webix_tree_close"]').click()

    action = ActionChains(driver)
    src = driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель"]')
    target = driver.find_element(By.XPATH, '//div[text()="Состояние:"]//parent::div//following-sibling::div//input')
    action.drag_and_drop(src, target)
    action.perform()


    cmd = driver.find_element(By.XPATH, '//div[text()="Команды:"]')
    scrl = driver.find_element(By.XPATH, '//div[text()="Цвет заливки:"]')
    driver.execute_script("arguments[0].scrollIntoView();", cmd)
    cmd.click()
    driver.execute_script("arguments[0].scrollIntoView();", scrl)

    driver.find_element(By.XPATH, '//b[text()="Modbus TCP"]/ancestor::div[@class="webix_tree_branch_2"]//b[text()="Выкатной выключатель"]/ancestor::span/preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель"]//ancestor::div[@class="webix_tree_branch_3"]//span[text()="Команды"]//preceding-sibling::div[@class="webix_tree_close"]').click()

    down = driver.find_element(By.XPATH, '//span[text()="Test_OFF"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    commands = driver.find_elements(By.XPATH, '//span[text()="Команды"]/ancestor::div[@class="webix_tree_branch_4"]//div[@class="webix_tree_branch_5"]')
    for i in commands:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.XPATH, '//div[@role="tabpanel"]//div[@role="listbox"]')
        action.drag_and_drop(src, target)
        action.perform()

    time.sleep(0.3)
    driver.find_element(By.CSS_SELECTOR, '.webix_tree_branch_3 .webix_tree_open').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()
    time.sleep(0.3)

    driver.find_element(By.CSS_SELECTOR, '.tbl13').click()
    time.sleep(1)


    cfg_btn.click()

    driver.find_element(By.XPATH, '//b[text()="Измерения"]//ancestor::span//preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//span[text()="Оперативная информация"]/preceding-sibling::div[@class="webix_tree_close"]').click()

    down = driver.find_element(By.XPATH, '//b[text()="Modbus TCP"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    measures = driver.find_elements(By.CSS_SELECTOR, '.webix_tree_branch_5')
    for i in measures:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.CSS_SELECTOR, '.webix_accordionitem_body .webix_view.webix_list')
        action.drag_and_drop(src, target)
        action.perform()
        
    driver.find_element(By.XPATH, '//b[text()="Modbus TCP"]/ancestor::div[@role="treeitem"]/div[@class="webix_tree_open"]').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()

    # IEC-101

    a_2 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='2536']")
    action = ActionChains(driver)
    action.double_click(on_element = a_2)
    action.perform()

    cfg_btn.click()
    driver.find_element(By.XPATH, '//b[text()="IEC-101"]//parent::span//preceding-sibling::div[@class="webix_tree_close"]').click()

    action = ActionChains(driver)
    src = driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель"]')
    target = driver.find_element(By.XPATH, '//div[text()="Состояние:"]//parent::div//following-sibling::div//input')
    action.drag_and_drop(src, target)
    action.perform()

    cmd = driver.find_element(By.XPATH, '//div[text()="Команды:"]')
    scrl = driver.find_element(By.XPATH, '//div[text()="Цвет заливки:"]')
    driver.execute_script("arguments[0].scrollIntoView();", cmd)
    cmd.click()
    driver.execute_script("arguments[0].scrollIntoView();", scrl)

    driver.find_element(By.XPATH, '//b[text()="IEC-101"]/ancestor::div[@class="webix_tree_branch_2"]//b[text()="Выкатной выключатель"]/ancestor::span/preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель"]//ancestor::div[@class="webix_tree_branch_3"]//span[text()="Команды"]//preceding-sibling::div[@class="webix_tree_close"]').click()
    down = driver.find_element(By.XPATH, '//span[text()="Test_OFF_Включить"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    commands = driver.find_elements(By.XPATH, '//span[text()="Команды"]/ancestor::div[@class="webix_tree_branch_4"]//div[@class="webix_tree_branch_5"]')
    for i in commands:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.XPATH, '//div[@role="tabpanel"]//div[@role="listbox"]')
        action.drag_and_drop(src, target)
        action.perform()



    driver.find_element(By.CSS_SELECTOR, '.webix_tree_branch_3 .webix_tree_open').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()


    a_3 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='2585']")
    action = ActionChains(driver)
    action.double_click(on_element = a_3)
    action.perform()

    cfg_btn.click()

    action = ActionChains(driver)
    src = driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель(DPI)"]')
    target = driver.find_element(By.XPATH, '//div[text()="Состояние:"]//parent::div//following-sibling::div//input')
    action.drag_and_drop(src, target)
    action.perform()

    cmd = driver.find_element(By.XPATH, '//div[text()="Команды:"]')
    scrl = driver.find_element(By.XPATH, '//div[text()="Цвет заливки:"]')
    driver.execute_script("arguments[0].scrollIntoView();", cmd)
    cmd.click()
    driver.execute_script("arguments[0].scrollIntoView();", scrl)

    driver.find_element(By.XPATH, '//b[text()="IEC-101"]/ancestor::div[@class="webix_tree_branch_2"]//b[text()="Выкатной выключатель(DPI)"]/ancestor::span/preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель(DPI)"]//ancestor::div[@class="webix_tree_branch_3"]//span[text()="Команды"]//preceding-sibling::div[@class="webix_tree_close"]').click()
    down = driver.find_element(By.XPATH, '//span[text()="Test_OFF_Включить"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    commands = driver.find_elements(By.XPATH, '//span[text()="Команды"]/ancestor::div[@class="webix_tree_branch_4"]//div[@class="webix_tree_branch_5"]')
    for i in commands:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.XPATH, '//div[@role="tabpanel"]//div[@role="listbox"]')
        action.drag_and_drop(src, target)
        action.perform()

    driver.find_element(By.CSS_SELECTOR, '.webix_tree_branch_3 .webix_tree_open').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()

    driver.find_element(By.CSS_SELECTOR, '.tbl8').click()
    time.sleep(1)
    cfg_btn.click()
    driver.find_element(By.XPATH, '//b[text()="Измерения"]//ancestor::span//preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//span[text()="Оперативная информация"]/preceding-sibling::div[@class="webix_tree_close"]').click()

    down = driver.find_element(By.XPATH, '//b[text()="IEC-101"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    measures = driver.find_elements(By.CSS_SELECTOR, '.webix_tree_branch_5')
    for i in measures:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.CSS_SELECTOR, '.webix_accordionitem_body .webix_view.webix_list')
        action.drag_and_drop(src, target)
        action.perform()
        
    driver.find_element(By.XPATH, '//b[text()="IEC-101"]/ancestor::div[@role="treeitem"]/div[@class="webix_tree_open"]').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()

    # IEC-104


    a_5 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='2937']")
    action = ActionChains(driver)
    action.double_click(on_element = a_5)
    action.perform()

    cfg_btn.click()
    driver.find_element(By.XPATH, '//b[text()="IEC-104"]//parent::span//preceding-sibling::div[@class="webix_tree_close"]').click()

    action = ActionChains(driver)
    src = driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель(DPI)"]')
    target = driver.find_element(By.XPATH, '//div[text()="Состояние:"]//parent::div//following-sibling::div//input')
    action.drag_and_drop(src, target)
    action.perform()

    cmd = driver.find_element(By.XPATH, '//div[text()="Команды:"]')
    scrl = driver.find_element(By.XPATH, '//div[text()="Цвет заливки:"]')
    driver.execute_script("arguments[0].scrollIntoView();", cmd)
    cmd.click()
    driver.execute_script("arguments[0].scrollIntoView();", scrl)

    driver.find_element(By.XPATH, '//b[text()="IEC-104"]/ancestor::div[@class="webix_tree_branch_2"]//b[text()="Выкатной выключатель(DPI)"]/ancestor::span/preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель(DPI)"]//ancestor::div[@class="webix_tree_branch_3"]//span[text()="Команды"]//preceding-sibling::div[@class="webix_tree_close"]').click()
    down = driver.find_element(By.XPATH, '//span[text()="Test_OFF_Включить"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    commands = driver.find_elements(By.XPATH, '//span[text()="Команды"]/ancestor::div[@class="webix_tree_branch_4"]//div[@class="webix_tree_branch_5"]')
    for i in commands:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.XPATH, '//div[@role="tabpanel"]//div[@role="listbox"]')
        action.drag_and_drop(src, target)
        action.perform()

    driver.find_element(By.CSS_SELECTOR, '.webix_tree_branch_3 .webix_tree_open').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()


    a_6 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='2989']")
    action = ActionChains(driver)
    action.double_click(on_element = a_6)
    action.perform()

    cfg_btn.click()

    action = ActionChains(driver)
    src = driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель"]')
    target = driver.find_element(By.XPATH, '//div[text()="Состояние:"]//parent::div//following-sibling::div//input')
    action.drag_and_drop(src, target)
    action.perform()

    cmd = driver.find_element(By.XPATH, '//div[text()="Команды:"]')
    scrl = driver.find_element(By.XPATH, '//div[text()="Цвет заливки:"]')
    driver.execute_script("arguments[0].scrollIntoView();", cmd)
    cmd.click()
    driver.execute_script("arguments[0].scrollIntoView();", scrl)

    driver.find_element(By.XPATH, '//b[text()="IEC-104"]/ancestor::div[@class="webix_tree_branch_2"]//b[text()="Выкатной выключатель"]/ancestor::span/preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//b[text()="Выкатной выключатель"]//ancestor::div[@class="webix_tree_branch_3"]//span[text()="Команды"]//preceding-sibling::div[@class="webix_tree_close"]').click()
    down = driver.find_element(By.XPATH, '//span[text()="Test_OFF_Включить"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    commands = driver.find_elements(By.XPATH, '//span[text()="Команды"]/ancestor::div[@class="webix_tree_branch_4"]//div[@class="webix_tree_branch_5"]')
    for i in commands:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.XPATH, '//div[@role="tabpanel"]//div[@role="listbox"]')
        action.drag_and_drop(src, target)
        action.perform()

    driver.find_element(By.CSS_SELECTOR, '.webix_tree_branch_3 .webix_tree_open').click()
    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()


    driver.find_element(By.CSS_SELECTOR, '.tbl17').click()

    cfg_btn.click()

    driver.find_element(By.XPATH, '//b[text()="Измерения"]//ancestor::span//preceding-sibling::div[@class="webix_tree_close"]').click()
    driver.find_element(By.XPATH, '//span[text()="Оперативная информация"]/preceding-sibling::div[@class="webix_tree_close"]').click()

    down = driver.find_element(By.XPATH, '//b[text()="IEC-104"]')
    driver.execute_script("arguments[0].scrollIntoView();", down)

    measures = driver.find_elements(By.CSS_SELECTOR, '.webix_tree_branch_5')
    for i in measures:
        action = ActionChains(driver)
        src = i
        target = driver.find_element(By.CSS_SELECTOR, '.webix_accordionitem_body .webix_view.webix_list')
        action.drag_and_drop(src, target)
        action.perform()

    driver.find_element(By.CSS_SELECTOR, '.wxi-close').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//a[text()="Схема"]').click()
    driver.find_element(By.XPATH, '//td[text()="Сохранить"]').click()
    time.sleep(1)

    driver.get(page_schemas)
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//button[text()="Сохранить проект"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Закрыть"]')))
    driver.find_element(By.XPATH, '//button[text()="Закрыть"]').click()

    print(time.asctime(), 'test_2002 создание привязок сигналов к графическим объектам пройден') 
