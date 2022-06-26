from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

def project_save(driver):
    driver.implicitly_wait(3)
    try:
        driver.find_element(By.XPATH, "//button[text()='Сохранить']").click()
        time.sleep(1)
        driver.find_element(By.XPATH, "//button[text()='Сохранить проект']").click()
        driver.switch_to.parent_frame()

        WebDriverWait(driver, 7).until(EC.element_to_be_clickable((By.XPATH, "//div[@view_id='project-events-window']//button")))
        btn = driver.find_element(By.XPATH, "//div[@view_id='project-events-window']//button")
        btn.click()
    finally:
        time.sleep(1)
