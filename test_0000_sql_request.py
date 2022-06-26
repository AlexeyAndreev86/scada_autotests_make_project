import psycopg2
import time

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database=db_name,
            user=db_user,
            password=db_password,
            host=db_host,
            port=db_port,
        )
        print("Connection successful")
    except:
        print("Error")
    return connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        cursor.close()
        return result
    except:
        print("Error")



def test_check_files_in_BD():
    select_files = 'SELECT name FROM fle."DEVICES"'
    files_to_search = ['Modbus.xml', 'Modbus.xml', 'МЭК-101 v1.xml', 'МЭК-104 v1.xml',
                      'Электрогенератор_100V_5A.xml', 'Bdps_TU_TS.xml']


    connection = create_connection('wsmtdb', 'mt_system', '1', '127.0.0.1', '5432')



    files = execute_read_query(connection, select_files)
    files_bd = [files[i][0] for i in range(len(files))]
    
    connection.close()

    cnt=len(files_to_search)
    for i in files_bd:
        if len(files_to_search)==0:
            break
        if i in files_to_search:
            files_to_search.remove(i)
            cnt-=1
              
    if cnt > 0:
        print('В базе данных нет файлов XML')
        from put_files_in_db import put_files_in_db
        put_files_in_db()
        time.sleep(0.3)
        test_check_files_in_BD()
    elif cnt == 0:
        print('Файлы на месте')
    
