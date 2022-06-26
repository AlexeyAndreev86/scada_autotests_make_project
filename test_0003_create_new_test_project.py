from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pages


project_name = 'Контроль webScadaMT v1'
   

def create_and_download_intermidiate_project(driver):
    global intemidiate_project_name
    intemidiate_project_name = time.asctime().replace(':', '_')
   
    driver.find_element(By.CLASS_NAME, "fa-plus-square").click()
    driver.find_element(By.XPATH, "//label[text()='Наименование:']/following-sibling::input").send_keys(intemidiate_project_name)
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@aria-colindex='2' and text()='"+intemidiate_project_name+"']").click()
    driver.find_element(By.XPATH, "//button[text()='Загрузить']").click()
    driver.find_element(By.XPATH, "//div[text()='Да']").click()
    driver.find_element(By.XPATH, "//div[text()='Да']").click()
    time.sleep(1)
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Закрыть"]')))
    driver.find_element(By.XPATH, "//button[text()='Закрыть']").click()
    
    current_project = EC.presence_of_element_located((By.XPATH, "//div[@view_id='current_project']/div[contains(text(), '"+intemidiate_project_name+"')]"))
    WebDriverWait(driver, 12).until(current_project)


def delete_last_test_project(driver):
    driver.find_element(By.XPATH, "//div[@aria-colindex='2' and text()='"+project_name+"']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[contains(@class, 'webix_row_select')]/span[contains(@class, 'wxi-trash')]").click()
    driver.find_element(By.XPATH, "//div[text()='Да']").click()
    time.sleep(1)
    all_projects_in_repo = driver.find_elements(By.XPATH, "//div[@view_id='projects']//div[@column='1']/div[@aria-colindex='2']")
    all_projects = []
    for prj in all_projects_in_repo:
        all_projects.append(prj.text)
    #print(all_projects)

    time.sleep(1)    
    assert project_name not in all_projects, 'Предыдущий тестовый проект не удалён'


def create_and_download_new_empty_test_project(driver):
    driver.find_element(By.CLASS_NAME, "fa-plus-square").click()
    driver.find_element(By.XPATH, "//label[text()='Наименование:']/following-sibling::input").send_keys(project_name)
    driver.find_element(By.XPATH, "//button[text()='OK']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[@aria-colindex='2' and text()='"+project_name+"']").click()
    driver.find_element(By.XPATH, "//button[text()='Загрузить']").click()
    driver.find_element(By.XPATH, "//div[text()='Да']").click()
    driver.find_element(By.XPATH, "//div[text()='Да']").click()
    time.sleep(1)
    WebDriverWait(driver, 25).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Закрыть"]')))
    driver.find_element(By.XPATH, "//button[text()='Закрыть']").click()

    loaded_project = driver.find_element(By.XPATH, '//div[@view_id="current_project"]/div[@class="webix_el_box"]').text
    loaded_project = loaded_project.split(':')[1].strip()

    assert loaded_project == project_name, 'Тестовый проект не загрузился'
    print(time.asctime(), 'Загружен проект:', loaded_project)


def delete_intermidiate_project(driver):
    global intemidiate_project_name
    driver.find_element(By.XPATH, "//div[@aria-colindex='2' and text()='"+intemidiate_project_name+"']").click()
    time.sleep(1)
    driver.find_element(By.XPATH, "//div[contains(@class, 'webix_row_select')]/span[contains(@class, 'wxi-trash')]").click()
    driver.find_element(By.XPATH, "//div[text()='Да']").click()
    time.sleep(0.25)
    try:
        
        all_projects_in_repo = driver.find_elements(By.XPATH, "//div[@view_id='projects']//div[@column='1']/div[@aria-colindex='2']")
        all_projects = []
        for prj in all_projects_in_repo:
            all_projects.append(prj.text)
    except:
        driver.refresh()
        print('refresh page')
        all_projects_in_repo = driver.find_elements(By.XPATH, "//div[@view_id='projects']//div[@column='1']/div[@aria-colindex='2']")
        all_projects = []
        for prj in all_projects_in_repo:
            all_projects.append(prj.text)
            
    time.sleep(1)
    assert intemidiate_project_name not in all_projects, 'Промежуточный проект не удалён'



#main function
def test_create_new_test_project(driver):
    print(time.asctime(), '\nТестирование создание проектов SCADA.mtp')
    time.sleep(1)
    driver.implicitly_wait(3)
    project_page = pages.project_page
    driver.get(project_page)
    time.sleep(1)
    title = driver.title
    
    if title == 'WebScadaMT':
        from autorization import autorization
        autorization(driver)
    
    current_project = driver.find_element(By.XPATH, '//div[@view_id="current_project"]/div[@class="webix_el_box"]').text
    current_project = current_project.split(':')[1].strip()

    all_projects_in_repo = driver.find_elements(By.XPATH, "//div[@view_id='projects']//div[@column='1']/div[@aria-colindex='2']")
    all_projects = []
    for prj in all_projects_in_repo:
        all_projects.append(prj.text)

    print(time.asctime(), 'Загружен проект:', current_project)
        
    if project_name == current_project:
        print(time.asctime(), 'Будет удалён старый тестовый проект "'+project_name+'" и создан новый')
        create_and_download_intermidiate_project(driver)
        delete_last_test_project(driver)
        create_and_download_new_empty_test_project(driver)
        delete_intermidiate_project(driver)
        time.sleep(1)
        print(time.asctime(), 'test_0002_create_new_test_project пройден')
    else:
        if project_name in all_projects:
            print('Старый тестовый проект, присутствующий в репозитории проектов будет удалён')
            delete_last_test_project(driver)
            create_and_download_new_empty_test_project(driver)
            time.sleep(1)
            print(time.asctime(), 'test_0002_create_new_test_project пройден')
        else:
            print(time.asctime(), 'Будет создан новый тестовый проект')
            create_and_download_new_empty_test_project(driver)
            time.sleep(1)
            print(time.asctime(), 'test_0002_create_new_test_project пройден')
            
