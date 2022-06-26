from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pages


def test_make_new_scheme(driver):
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

    print(time.asctime(), 'создаём мнемосхему проекта')

    old_schemas = driver.find_elements(By.CSS_SELECTOR, 'div[aria-colindex="2"]')
    if len(old_schemas)>0:
        driver.find_element(By.CSS_SELECTOR, 'span[title="Удалить все"]').click()
        driver.find_element(By.XPATH, '//div[text()="Да"]').click()
        time.sleep(1)

    time.sleep(0.5)
    try:
        driver.find_element(By.XPATH, '//button[text()="Добавить схему"]').click()
    except:
        driver.refresh()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//button[text()="Добавить схему"]').click()
    driver.find_element(By.TAG_NAME, 'input').send_keys('Контроль модулей')
    driver.find_element(By.XPATH, '//button[text()="OK"]').click()

        
    time.sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, '.wxi-pencil').click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geSprite.geSprite-link')))

    driver.find_element(By.XPATH, '//a[text()="Дополнительно"]').click()
    time.sleep(0.1)
    driver.find_element(By.XPATH, '//td[text()="Редактировать схему..."]').click()
    WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.geDialog textarea')))
    driver.find_element(By.CSS_SELECTOR, '.geDialog textarea').clear()
    driver.find_element(By.CSS_SELECTOR, '.geDialog textarea').click()
    import nest
    s = nest.schema
    new_s = 0
    cnt = 0
    # каркас схемы вставляем как текст, привязки будем параметрировать позже
    # текст будет вставляться 2 минуты
    while new_s<len(s):
        chunk=s[cnt:cnt+128]
        new_s+=len(chunk)
        cnt+=128
        driver.find_element(By.TAG_NAME, 'textarea').send_keys(chunk)

    time.sleep(1)
    driver.find_element(By.XPATH, '//button[text()="OK"]').click()
    time.sleep(2)
    driver.find_element(By.XPATH, '//a[text()="Схема"]').click()
    driver.find_element(By.XPATH, '//td[text()="Сохранить"]').click()
    time.sleep(2)
    
    driver.get(page_schemas)
    time.sleep(1)
    driver.find_element(By.XPATH, '//button[text()="Сохранить проект"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Закрыть"]')))
    driver.find_element(By.XPATH, '//button[text()="Закрыть"]').click()

    print(time.asctime(), 'test_2001 создание мнемосхемы проекта пройден') 
    time.sleep(1)
    
