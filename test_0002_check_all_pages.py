from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from pages import *


def test_checki_all_pages(driver):
    
    pages = [project_page, page_exchange, page_equipments, page_schemas,
             page_trend, page_db_service, page_users, page_events, page_reports]

    title_list_etalon = ['Домашняя страница', 'Конфигуратор модулей', 'Редактор оборудования', 'Мнемосхемы', 'База данных', 'Обслуживание БД', 'Пользователи', 'События', 'Отчёты']
    title_list = []
    errors_list = []
    
    try:
        driver.implicitly_wait(3)
        driver.get(project_page)
        time.sleep(1)
        title = driver.title
            
        if title == 'WebScadaMT':
            from autorization import autorization
            autorization(driver)
            time.sleep(1)


        for page in pages:
            driver.get(page)
            time.sleep(2)
            title = driver.title
            title_list.append(title)

        assert len(title_list) == 9, "Количество заголовков страниц должно 9"

        for i in range(len(title_list)):
            if title_list[i] != title_list_etalon[i]:
                errors_list.append(title_list_etalon[i])
        
        if len(errors_list)>0:
            print('Проблема со вкладками:', errors_list)

        assert len(errors_list) == 0, f'Проверьте вкладки {errors_list}'
        
    finally:
        print(time.asctime(), 'test_0002 проверка всех вкладок SCADA пройден')
