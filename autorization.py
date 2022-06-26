'''
Данная функцию нужна для повторной регистрации после падения какого-либо автотеста.
'''


from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

def autorization(driver):
    driver.implicitly_wait(3)
    try:
        print(time.asctime(), '\n!!! проходим авторизацию autorization.py')
        driver.find_element(By.XPATH, "//input[@placeholder='Логин']").send_keys('system')
        driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys('1')
        driver.find_element(By.XPATH, "//button[text()='Вход']").click()
    finally:
        time.sleep(1)
