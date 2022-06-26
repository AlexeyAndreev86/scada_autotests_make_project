from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import pages

       
def test_autorization(driver):

    link = pages.page_main
    driver.get(link)
    driver.implicitly_wait(2)
    time.sleep(1)
    assert "WebScadaMT" in driver.title, "Страница не загружена"    
  
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин"]').send_keys('Director')
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').send_keys('qwertry')
    driver.find_element(By.XPATH, '//button[text()="Вход"]').click()
    autorization_error=driver.find_element(By.CSS_SELECTOR, '.webix_message_area').text
    assert "Ошибка авторизации" in autorization_error, "SCADA принимает неверный логин+пароль"
    time.sleep(3)
  
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин"]').send_keys('system')
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').send_keys('808aqw')
    driver.find_element(By.XPATH, '//button[text()="Вход"]').click()
    autorization_error=driver.find_element(By.CSS_SELECTOR, '.webix_message_area').text
    assert "Ошибка авторизации" in autorization_error, "SCADA принимает неверный пароль"    
    time.sleep(3)
   
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин"]').clear()   
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Логин"]').send_keys('system')
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').clear()
    driver.find_element(By.CSS_SELECTOR, 'input[placeholder="Пароль"]').send_keys('1' + Keys.ENTER)
    

    # ставим галочку РЕЖИМ ОТЛАДКИ
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[@button_id="tabSettings"]').click()
    time.sleep(0.5)
    debug = driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Режим отладки:"]').get_attribute('aria-checked')
    if debug == 'false':
        driver.find_element(By.CSS_SELECTOR, 'button[aria-label="Режим отладки:"]').click()
        print('Установлен режим отладки')


    time.sleep(0.5)
    assert "Домашняя страница" in driver.title, "Авторизация не пройдена"
    
