from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.action_chains import ActionChains
import pages


def test_calc_tags(driver):
    page_exchange = pages.page_exchange

    driver.implicitly_wait(3)
    driver.get(page_exchange)
    time.sleep(1)
    title = driver.title
    
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
        driver.get(page_exchange)
    

    print(time.asctime(), '\nПараметрируем вычисляемые параметры')
    time.sleep(0.75)

    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Вычисляемые параметры')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        # обновляем страницу в случае StaleElementReferenceException (перестраивается DOM-структура страницы)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Вычисляемые параметры')]").click()

    driver.switch_to.frame(0)

    autostart = driver.find_element(By.XPATH, '//button[@aria-label="Автозапуск:"]').get_attribute('aria-checked')
    if autostart == 'false':
        driver.find_element(By.XPATH, "//label[text()='Автозапуск:']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)

    driver.find_element(By.XPATH, "//div[@button_id='tab_groups']").click()
    groups = driver.find_elements(By.XPATH, '//div[@aria-colindex="3"]')
    if len(groups)>0:
        print('удаляем все группы, входящие в модуль ВЫЧИСЛЯЕМЫЕ ПАРАМЕТРЫ')
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@title='Удалить все']").click()
        driver.find_element(By.XPATH, "//div[text()='Да']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Добавить группу']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Добавить группу']").click()
    time.sleep(1)

    new_group_name = driver.find_element(By.XPATH, "//div[@aria-rowindex='1' and @aria-colindex='3']")
    new_group_name.click()
    action = ActionChains(driver)
    new_group_name_2 = driver.find_element(By.XPATH, "//div[@aria-rowindex='1' and @aria-colindex='3']")
    action.double_click(on_element=new_group_name_2)
    action.perform()
    driver.find_element(By.XPATH, "//input[@aria-label='Группа']").send_keys('DPI' + Keys.ENTER)
    time.sleep(1)

    new_group_name1 = driver.find_element(By.XPATH, "//div[@aria-rowindex='2' and @aria-colindex='3']")
    new_group_name1.click()
    action = ActionChains(driver)
    new_group_name_21 = driver.find_element(By.XPATH, "//div[@aria-rowindex='2' and @aria-colindex='3']")
    action.double_click(on_element=new_group_name_21)
    action.perform()
    driver.find_element(By.XPATH, "//input[@aria-label='Группа']").send_keys('Float' + Keys.ENTER)
    time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(1)
    driver.find_element(By.TAG_NAME, "a").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, 'div[button_id="tab_tags"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@class="webix_view webix_accordionitem collapsed horizontal params_tree_acc"]').click()

    driver.find_element(By.XPATH, '//button[text()="Добавить параметр"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="3"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('DPI' + Keys.ENTER)
    driver.find_element(By.TAG_NAME, "textarea").send_keys('(')
    driver.find_element(By.XPATH, '//b[text()="VirtualDevices"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="Имитатор"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="Device1"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="Parameter"]').click()

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[text()="RPV"]')
    target = driver.find_element(By.TAG_NAME, "textarea")
    action.drag_and_drop(source, target).perform()

    driver.find_element(By.TAG_NAME, "textarea").send_keys(' & (!')

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[text()="RPO"]')
    target = driver.find_element(By.TAG_NAME, "textarea")
    action.drag_and_drop(source, target).perform()

    driver.find_element(By.TAG_NAME, "textarea").send_keys(')) == 1? 2:1')

    driver.find_element(By.XPATH, '//div[@class="webix_tree_open webix_sub_open"]').click()
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, '//button[text()="Добавить параметр"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="3"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('SPI_OFF' + Keys.ENTER)

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[text()="RPO"]')
    target = driver.find_element(By.TAG_NAME, "textarea")
    action.drag_and_drop(source, target).perform()

    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(2.7)
    # кнопка "Добавить проект" под всплывающими сообщениями, ждём пока они уйдут

    driver.find_element(By.XPATH, '//button[text()="Добавить параметр"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="3"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('SPI_ON' + Keys.ENTER)

    action = ActionChains(driver)
    source = driver.find_element(By.XPATH, '//span[text()="RPV"]')
    target = driver.find_element(By.TAG_NAME, "textarea")
    action.drag_and_drop(source, target).perform()

    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="5"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="2" and @aria-colindex="5"]').click()
    driver.find_element(By.XPATH, '//select/option[@value="3"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="5"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="5"]').click()
    driver.find_element(By.XPATH, '//select/option[@value="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-rowindex="3" and @aria-colindex="6"]').click()
    time.sleep(0.5)

    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(1)

    driver.switch_to.parent_frame()

    group_float = driver.find_element(By.XPATH, '//span[text()="Float"]')
    driver.execute_script("return arguments[0].scrollIntoView(true);", group_float)
    group_float.click()

    driver.switch_to.frame(0)

    driver.find_element(By.CSS_SELECTOR, 'div[button_id="tab_tags"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@class="webix_view webix_accordionitem collapsed horizontal params_tree_acc"]').click()

    driver.find_element(By.XPATH, '//button[text()="Добавить параметр"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="3"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('Float')
    driver.find_element(By.XPATH, '//div[@aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="4"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('Float')
    driver.find_element(By.XPATH, '//div[@aria-colindex="5"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="5"]').click()
    driver.find_element(By.XPATH, '//select/option[@value="2"]').click()
    driver.find_element(By.XPATH, '//b[text()="DatabaseTags"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//b[text()="Group"]').click()
    time.sleep(0.5)
    driver.find_element(By.TAG_NAME, "textarea").click()
    driver.find_element(By.XPATH, "//span[contains(text(), '(Test)')]//following-sibling::span[@title='Добавить параметр']").click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//div[@aria-expanded="true"]/div[@class="webix_tree_open webix_sub_open"]').click()

    x = 2
    for i in range(2,7):
        time.sleep(0.85)
        driver.find_element(By.XPATH, '//button[text()="Добавить параметр"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(i)+'" and @aria-colindex="3"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(i)+'" and @aria-colindex="3"]').click()
        driver.find_element(By.TAG_NAME, "input").send_keys('Float'+str(x))
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(i)+'" and @aria-colindex="4"]').click()
        driver.find_element(By.TAG_NAME, "input").send_keys('Float'+str(x))
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(i)+'" and @aria-colindex="5"]').click()
        driver.find_element(By.XPATH, '//div[@aria-rowindex="'+str(i)+'" and @aria-colindex="5"]').click()
        driver.find_element(By.XPATH, '//select/option[@value="2"]').click()
        time.sleep(0.5)
        driver.find_element(By.TAG_NAME, "textarea").send_keys("'DatabaseTags.Group.Test'*"+str(x))
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//div[@aria-expanded="true"]/div[@class="webix_tree_open webix_sub_open"]').click()
        x *= 2

    from project_save import project_save
    project_save(driver)

    print(time.asctime(), 'test_0006_exchange_calc_tags пройден')
