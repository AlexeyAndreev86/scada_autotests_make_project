from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import pages


def test_database_tags(driver):
    page_exchange = pages.page_exchange

    driver.implicitly_wait(3)
    driver.get(page_exchange)
    time.sleep(1)
    title = driver.title
    
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
        driver.get(page_exchange)
    
    print(time.asctime(), '\nПараметрируем сохраняемые параметры')
    time.sleep(0.75)
    
    try:
        driver.find_element(By.XPATH, "//span[contains(text(), 'Сохраняемые параметры')]").click()
    except:
        print('устаревший элемент DOM')
        time.sleep(1)
        # обновляем страницу в случае StaleElementReferenceException (перестраивается DOM-структура страницы)
        driver.refresh()
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[contains(text(), 'Сохраняемые параметры')]").click()


    driver.switch_to.frame(0)

    autostart = driver.find_element(By.XPATH, '//button[@aria-label="Автозапуск:"]').get_attribute('aria-checked')
    if autostart == 'false':
        driver.find_element(By.XPATH, "//label[text()='Автозапуск:']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)

    driver.find_element(By.XPATH, "//div[@button_id='tab_groups']").click()
    groups = driver.find_elements(By.XPATH, '//div[@aria-colindex="3"]')
    if len(groups)>0:
        print('удаляем все группы, входящие в модуль СОХРАНЯЕМЫЕ ПАРАМЕТРЫ')
        time.sleep(1)
        driver.find_element(By.XPATH, "//span[@title='Удалить все']").click()
        driver.find_element(By.XPATH, "//div[text()='Да']").click()
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)

    driver.find_element(By.XPATH, "//button[text()='Добавить группу']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
    time.sleep(1)
    driver.find_element(By.TAG_NAME, "a").click()
    time.sleep(1)

    driver.find_element(By.CSS_SELECTOR, 'div[button_id="tab_tags"]').click()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//button[text()="Добавить параметр"]').click()

    driver.find_element(By.XPATH, '//div[@aria-colindex="2"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="2"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('Test' + Keys.ENTER)

    driver.find_element(By.XPATH, '//div[@aria-colindex="3"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="3"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('Test' + Keys.ENTER)

    driver.find_element(By.XPATH, '//div[@aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="4"]').click()
    driver.find_element(By.XPATH, '//select/option[text()="Целочисленное"]').click()

    driver.find_element(By.XPATH, '//div[@aria-colindex="5"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('2' + Keys.ENTER)

    driver.find_element(By.XPATH, '//div[@aria-colindex="6"]').click()
    driver.find_element(By.XPATH, '//div[@aria-colindex="6"]').click()
    driver.find_element(By.TAG_NAME, "input").send_keys('Гц' + Keys.ENTER)

    from project_save import project_save
    project_save(driver)

    print(time.asctime(), 'test_0005_exchange_database_tags пройден')
