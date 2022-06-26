from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pages


def test_equipments_tree(driver):
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

    print(time.asctime(), '\nначинаем параметризацию вкладки ОБОРУДОВАНИЕ')    
    time.sleep(1)

    add_equipment = driver.find_element(By.XPATH, "//div[@view_id='add']//span[contains(@class, 'fa-plus-square')]")
    delete_equipment = driver.find_element(By.CSS_SELECTOR, ".fa-trash-alt")



    # скрипт скроллинга встроенного контейнера (можно убрать, так как второй скрипт выберет элемент без прокрутки, оставлю на память)
    scroll = "var scroll = document.querySelector(\'div.webix_vscroll_y\'); if(scroll != null) { \tscroll.scrollTop = (scroll.scrollHeight / 2); }"
    # скрипт выбора невидимого span во встроенном контейнере без скроллинга
    oborud = '$$("templateList").select("Оборудование")'


    equips = driver.find_elements(By.CSS_SELECTOR, 'div[aria-level="1"]')
    # удаляем старое оборудование, если оно есть
    if len(equips)>0:
        while len(equips)>0:        
            driver.find_element(By.CSS_SELECTOR, 'div[aria-level="1"]').click()
            delete_equipment.click()
            driver.find_element(By.XPATH, "//div[text()='Да']").click()
            equips = driver.find_elements(By.CSS_SELECTOR, 'div[aria-level="1"]')


    add_equipment.click()
    driver.execute_script(scroll)
    driver.execute_script(oborud)
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.find_element(By.CSS_SELECTOR, ".wxi-close").click()
    driver.find_element(By.XPATH, '//div[@aria-level="1"]/span[text()="Оборудование"]').click()
    add_equipment.click()


    protocols = ['Modbus RTU', 'Modbus TCP', 'IEC-101', 'IEC-104']
    for i in range(len(protocols)):
        driver.execute_script(oborud)
        driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.find_element(By.CSS_SELECTOR, ".wxi-close").click()
    time.sleep(0.3)


    driver.find_element(By.XPATH, '//div[@aria-level="1"]/span[text()="Оборудование"]').click()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').clear()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').send_keys('Тест WebScadaMT')
    time.sleep(0.3)
    

    second_line_equips = driver.find_elements(By.CSS_SELECTOR, 'div[aria-level="2"]')

    for i in range(len(second_line_equips)):
        second_line_equips[i].click()
        driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').clear()
        driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').send_keys(protocols[i])
        time.sleep(0.3)

    # создаём оборудование третей степени вложенности

    driver.find_element(By.XPATH, '//span[text()="Modbus RTU"]').click()
    add_equipment.click()
    driver.execute_script('$$("templateList").select("Выключатель")')
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.execute_script(oborud)
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.find_element(By.CSS_SELECTOR, ".wxi-close").click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-level="3"]//span[text()="Оборудование"]').click()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').clear()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').send_keys('Измерения')
    time.sleep(0.3)

    driver.find_element(By.XPATH, '//span[text()="Modbus TCP"]').click()
    add_equipment.click()
    driver.execute_script('$$("templateList").select("Выкатной выключатель")')
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.execute_script(oborud)
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.find_element(By.CSS_SELECTOR, ".wxi-close").click()
    time.sleep(0.3)
    driver.find_element(By.XPATH, '//div[@aria-level="3"]//span[text()="Оборудование"]').click()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').clear()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').send_keys('Измерения')
    time.sleep(0.3)

    driver.find_element(By.XPATH, '//span[text()="IEC-101"]').click()
    add_equipment.click()
    driver.execute_script('$$("templateList").select("Выкатной выключатель(DPI)")')
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(0.1)
    driver.execute_script('$$("templateList").select("Выкатной выключатель")')
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(0.1)
    driver.execute_script(oborud)
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.find_element(By.CSS_SELECTOR, ".wxi-close").click()
    driver.find_element(By.XPATH, '//div[@aria-level="3"]//span[text()="Оборудование"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').clear()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').send_keys('Измерения')
    time.sleep(0.3)

    driver.find_element(By.XPATH, '//span[text()="IEC-104"]').click()
    add_equipment.click()
    driver.execute_script('$$("templateList").select("Выкатной выключатель(DPI)")')
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(0.1)
    driver.execute_script('$$("templateList").select("Выкатной выключатель")')
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(0.1)
    driver.execute_script(oborud)
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    driver.find_element(By.CSS_SELECTOR, ".wxi-close").click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//div[@aria-level="3"]//span[text()="Оборудование"]').click()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').clear()
    driver.find_element(By.XPATH, '//div[@view_id="eqName"]//input').send_keys('Измерения')
    time.sleep(0.3)

    driver.find_element(By.XPATH, '//button[text()="Сохранить"]').click()
    time.sleep(1)
    print(time.asctime(), 'test_1001_equipments_tree пройден')
    
    
    
