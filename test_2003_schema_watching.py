from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

import time
import pages


look_events = ['Включить', 'Включить', 'Включен', 'Отключить']
look_args = ['Тест WebScadaMT/IEC-104/Выкатной выключатель(DPI)', 'Тест WebScadaMT/IEC-104/Выкатной выключатель', 'Тест WebScadaMT/Modbus RTU/Выключатель', 'Тест WebScadaMT/Modbus RTU/Выключатель']


def test_scheme_watching(driver):
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

    print(time.asctime(), 'проверяем работу мнемосхемы')
    driver.find_element(By.TAG_NAME, "a").click()

    WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.TAG_NAME, 'svg')))

    
    breakers_ON = driver.find_elements(By.XPATH, '//*[name()="rect" and @fill="#640064"]')
    assert len(breakers_ON) == 6, "На мнемосхеме должно быть 6 выключателей во включённом положении!"

    # возможен StaleElementReferenceException
    try:
        breaker_1 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='503']")
        action = ActionChains(driver)
        action.context_click(on_element = breaker_1)
        action.perform()
        driver.find_element(By.XPATH, '//table//td[text()="Отключить"]').click()
    except:
        print('StaleElementReferenceException')
        breaker_1 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='503']")
        action = ActionChains(driver)
        action.context_click(on_element = breaker_1)
        action.perform()
        driver.find_element(By.XPATH, '//table//td[text()="Отключить"]').click()

    time.sleep(2)
    breakers_OFF = driver.find_elements(By.XPATH, '//*[name()="rect" and @stroke="white" and @height="20"]')
    assert len(breakers_OFF) == 6, "На мнемосхеме должно быть 6 выключателей в выключённом положении!"

    

    # возможен StaleElementReferenceException
    try:
        breaker_2 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='1106']")
        action = ActionChains(driver)
        action.context_click(on_element = breaker_2)
        action.perform()
        driver.find_element(By.XPATH, '//table//td[text()="Включить"]').click()
    except:
        print('StaleElementReferenceException')
        breaker_2 = driver.find_element(By.XPATH, "//*[name()='svg']//*[name()='rect' and @x='1106']")
        action = ActionChains(driver)
        action.context_click(on_element = breaker_2)
        action.perform()
        driver.find_element(By.XPATH, '//table//td[text()="Включить"]').click()

    timestamp = time.asctime().split()[3]
    print(timestamp)
    
    time.sleep(3.5)
    breakers_ON = driver.find_elements(By.XPATH, '//*[name()="rect" and @fill="#640064"]')
    assert len(breakers_ON) == 6, "На мнемосхеме должно быть 6 выключателей во включённом положении!"


    driver.find_element(By.CSS_SELECTOR, '.webix_badge').click()
    time.sleep(0.5)

    alarm_mess = driver.find_elements(By.CSS_SELECTOR, '.event_type_ERROR')
    assert len(alarm_mess)>=1, 'Не хватает аварийных сообщений в журнале'

    col_2 = driver.find_elements(By.XPATH, '//div[@aria-colindex="2"]')
    events = []
    for i in col_2[:4]:
        events.append(i.text)
    assert events == look_events, 'events'

    col_3 = driver.find_elements(By.XPATH, '//div[@aria-colindex="3"]')
    args = []
    for i in col_3[:4]:
        args.append(i.text)
    assert args == look_args, 'args'

    col_5 = driver.find_elements(By.XPATH, '//div[@aria-colindex="5"]')
    times = []
    for i in col_5[:4]:
        times.append(i.text[-12:-4])
    assert timestamp in times, 'times'

    time.sleep(3)
    print(time.asctime(), 'test_2003 проверка работы графической части мнемосхемы пройден') 
