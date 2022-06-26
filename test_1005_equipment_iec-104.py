from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pages


def breakers_commands(driver):
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and text()="Включить"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="tag_54"]').click()
    time.sleep(0.5)

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[text()="On"]')
    target = driver.find_element(By.CSS_SELECTOR, '.webix_cell_select')
    action.drag_and_drop(source, target).perform()
    time.sleep(0.5)

    driver.find_element(By.XPATH, '//b[text()="tag_54"]').click()
    time.sleep(0.75)
    driver.find_element(By.XPATH, '//b[text()="tag_53"]').click()
    time.sleep(0.75)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and text()="Отключить"]').click()

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[text()="On"]')
    target = driver.find_element(By.CSS_SELECTOR, '.webix_cell_select')
    action.drag_and_drop(source, target).perform()

    tags_nums = ['53', '50', '51', '52', '55', '56', '57', '58', '59']
    for i in range(1, len(tags_nums)):
        time.sleep(0.5)
        driver.find_element(By.CSS_SELECTOR, 'div[view_id="$button8"] .webix_button').click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//div[@view_id="tblCommands"]//div[@column="1"]/div[last()]').click()
        time.sleep(0.75)
        driver.find_element(By.XPATH, '//b[text()="tag_'+tags_nums[i-1]+'"]').click()
        time.sleep(0.75)
        driver.find_element(By.XPATH, '//b[text()="tag_'+tags_nums[i]+'"]').click()
        time.sleep(0.75)
        action = ActionChains(driver)
        source = driver.find_element(By.XPATH, '//span[text()="On"]')
        target = driver.find_element(By.CSS_SELECTOR, '.webix_cell_select')
        action.drag_and_drop(source, target).perform()



def test_equipment_IEC_104(driver):
    page_equipments = pages.page_equipments

    driver.implicitly_wait(3)
    driver.get(page_equipments)
    time.sleep(1)
    title = driver.title
        
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
        driver.get(page_equipments)
        time.sleep(1)

    print(time.asctime(), '\nпродолжаем параметризацию вкладки ОБОРУДОВАНИЕ')    
    time.sleep(1)

    driver.find_element(By.XPATH, '//div[@aria-level="2"]/span[text()="IEC-104"]//preceding-sibling::div[@class="webix_tree_close webix_tree_img webix_tree_plus2"]').click()
    driver.find_element(By.XPATH, "//span[text()='IEC-104']//ancestor::div[@class='webix_tree_branch_2']//span[text()='Выкатной выключатель(DPI)']").click()

    parameter_window = driver.find_element(By.XPATH, '//div[@class="webix_accordionitem_label" and text()="Параметры"]//parent::div[@webix_ai_id="params_tree_acc"]')
    params_expanded = parameter_window.get_attribute('aria-expanded')
    if params_expanded == 'false':
        parameter_window.click()

    time.sleep(0.75)
    driver.find_element(By.XPATH, '//b[text()="IEC104Client"]').click()
    time.sleep(0.75)
    driver.find_element(By.XPATH, '//b[text()="127_0_0_1_2404"]').click()
    time.sleep(0.75)
    driver.find_element(By.XPATH, '//b[text()="ASDU_3"]').click()
    time.sleep(0.75)
    driver.find_element(By.XPATH, '//b[text()="DiscreteSignals"]').click()
    time.sleep(0.75)

    service_window = driver.find_element(By.XPATH, '//div[@aria-label="Обслуживание"]/parent::div[@role="tab"]')
    service_expanded = service_window.get_attribute('aria-expanded')
    if service_expanded == 'false':
        service_window.click()

    driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Уведомления об обслуживании"]').click()
    time.sleep(0.25)
    driver.find_element(By.XPATH, '//select/option[text()="Параметр"]').click()

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[contains(., "(Контрольное)")]')
    target = driver.find_element(By.XPATH, '//div[@view_id="maintParamTable"]//div[@role="rowgroup"]')
    action.drag_and_drop(source, target).perform()

    driver.find_element(By.XPATH, "//span[text()='IEC-104']//ancestor::div[@class='webix_tree_branch_2']//span[text()='Выкатной выключатель']").click()
    driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Уведомления об обслуживании"]').click()
    time.sleep(0.25)
    driver.find_element(By.XPATH, '//select/option[text()="Параметр"]').click()
    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[contains(., "(Контрольное)")]')
    target = driver.find_element(By.XPATH, '//div[@view_id="maintParamTable"]//div[@role="rowgroup"]')
    action.drag_and_drop(source, target).perform()

    time.sleep(0.25)
    service_window.click()

    states_window =  driver.find_element(By.XPATH, '//div[@webix_ai_id="fieldStates"]')
    states_expanded = states_window.get_attribute('aria-expanded')
    if states_expanded == 'false':
        states_window.click()

    time.sleep(0.25)
    driver.find_element(By.XPATH, "//span[text()='IEC-104']//ancestor::div[@class='webix_tree_branch_2']//span[text()='Выкатной выключатель(DPI)']").click()

    time.sleep(0.25)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and text()="Состояние выключателя"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(DPI)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and text()="Тележка в рабочем положении"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(Рабочее)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and text()="Тележка в контрольном положении"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(Контрольное)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="4" and text()="Опер. блокировка"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(Опер блокировка)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="5" and text()="Ручное управление"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(МУ)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.25)


    driver.find_element(By.XPATH, "//span[text()='IEC-104']//ancestor::div[@class='webix_tree_branch_2']//span[text()='Выкатной выключатель']").click()

    time.sleep(0.25)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="1" and text()="Выключатель включен"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(SPI_ON_RPV)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and text()="Выключатель отключен"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(SPI_OFF_RPO)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and text()="Тележка в рабочем положении"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(Рабочее)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="4" and text()="Тележка в контрольном положении"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(Контрольное)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="5" and text()="Опер. блокировка"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(Опер блокировка)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="6" and text()="Ручное управление"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//span[contains(., "(МУ)")]//following-sibling::span[@title="Добавить параметр"]').click()
    time.sleep(0.25)

    states_window.click()

    oper_info_window = driver.find_element(By.CSS_SELECTOR, 'div[webix_ai_id="fieldOperInfo"]')
    oper_info_expanded = oper_info_window.get_attribute('aria-expanded')
    if oper_info_expanded == 'false':
        oper_info_window.click()

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//b[text()="DiscreteSignals"]')
    target = driver.find_element(By.CSS_SELECTOR, 'div[view_id="tblOperInfo"] .webix_ss_body')
    action.drag_and_drop(source, target).perform()
    time.sleep(0.25)

    driver.find_element(By.XPATH, "//span[text()='IEC-104']//ancestor::div[@class='webix_tree_branch_2']//span[text()='Выкатной выключатель(DPI)']").click()
    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//b[text()="DiscreteSignals"]')
    target = driver.find_element(By.CSS_SELECTOR, 'div[view_id="tblOperInfo"] .webix_ss_body')
    action.drag_and_drop(source, target).perform()
    time.sleep(0.25)

    oper_info_window.click()

    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="DiscreteSignals"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="Commands"]').click()
    time.sleep(0.5)

    commands_window = driver.find_element(By.CSS_SELECTOR, 'div[webix_ai_id="fieldCommands"]')
    commands_expanded = commands_window.get_attribute('aria-expanded')
    if commands_expanded == 'false':
        commands_window.click()


    breakers_commands(driver)
    driver.find_element(By.CSS_SELECTOR, '.settings-table-icon.question').click()
    driver.find_element(By.CSS_SELECTOR, '.settings-table-icon.question').click()
    driver.find_element(By.XPATH, '//b[text()="tag_59"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//span[text()='IEC-104']//ancestor::div[@class='webix_tree_branch_2']//span[text()='Выкатной выключатель']").click()
    breakers_commands(driver)
    driver.find_element(By.CSS_SELECTOR, '.settings-table-icon.question').click()
    driver.find_element(By.CSS_SELECTOR, '.settings-table-icon.question').click()


    commands_window = driver.find_element(By.CSS_SELECTOR, 'div[webix_ai_id="fieldCommands"]')
    commands_expanded = commands_window.get_attribute('aria-expanded')
    if commands_expanded == 'true':
        commands_window.click()


    # параметрируем Измерения
    driver.find_element(By.XPATH, "//span[text()='IEC-104']//ancestor::div[@class='webix_tree_branch_2']//span[text()='Измерения']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="Commands"]').click()

    oper_info_window = driver.find_element(By.CSS_SELECTOR, 'div[webix_ai_id="fieldOperInfo"]')
    oper_info_expanded = oper_info_window.get_attribute('aria-expanded')
    if oper_info_expanded == 'false':
        oper_info_window.click()

    time.sleep(1)
    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//b[text()="AnalogSignals"]')
    target = driver.find_element(By.CSS_SELECTOR, 'div[view_id="tblOperInfo"] .webix_ss_body')
    action.drag_and_drop(source, target).perform()


    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    driver.find_element(By.XPATH, "//button[text()='Сохранить проект']").click()
    print(time.asctime(), 'test_1005_equipments_IEC-104 пройден') 
    time.sleep(1)
