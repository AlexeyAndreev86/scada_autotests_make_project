def put_files_in_db():

    import requests
    from pages import url_version, url_login, url_file


    param_login = {"login": "system", "password": "1"}
    payload={'ftype': 'xml'}
    path = 'C:/andreev_autotests/'

    s = requests.Session()

    version = s.get(url_version, verify = False).text.replace('"', '')[:3]

    if version == '4.3':
        filetype = 'files'
    elif version == '4.2':
        filetype = 'files[]'

    # нужно постить не data (будет код 415), а json
    a = s.post(url_login, json = param_login, verify = False)


    # Закачиваем файлы виртуальных устройств
    param_file_virt_devices = {"mid": "efdaf28e-6698-41f1-93f7-85230f7f7a00", "sid": "null", "type": "DEV"}

    files_virt_devices= [(filetype, ('Bdps_TU_TS.xml', open(path+'Bdps_TU_TS.xml', 'rb'), 'text/xml')),
                         (filetype, ('Электрогенератор_100V_5A.xml', open(path+'Электрогенератор_100V_5A.xml', 'rb'), 'text/xml'))]
                                                                    
    virt_device = s.post(url_file, params=param_file_virt_devices, data=payload, files=files_virt_devices, verify=False)

    # Modbus RTU
    param_file_modbus_rtu = {"mid": "0c5679eb-7dc2-4e44-a404-ded13f7a37f9", "sid": "null", "type": "DEV"}
    files_modbus_rtu = [(filetype, ('Modbus.xml', open(path+'Modbus.xml', 'rb'), 'text/xml'))]                                                                
    modbus_rtu = s.post(url_file, params=param_file_modbus_rtu, data=payload, files=files_modbus_rtu, verify=False)

    # Modbus TCP
    param_file_modbus_tcp = {"mid": "67b1dcff-0f36-476e-a91f-a02cc4500715", "sid": "null", "type": "DEV"}
    files_modbus_tcp = [(filetype, ('Modbus.xml', open(path+'Modbus.xml', 'rb'), 'text/xml'))] 
    modbus_rtu = s.post(url_file, params=param_file_modbus_tcp, data=payload, files=files_modbus_tcp, verify=False)

    # IEC-101
    param_file_iec_101 = {"mid": "05146dd2-6749-4d0b-b74e-a68aa1376a68", "sid": "null", "type": "DEV"}
    files_iec_101 = [(filetype, ('МЭК-101 v1.xml', open(path+'МЭК-101 v1.xml', 'rb'), 'text/xml'))]                                                                
    modbus_rtu = s.post(url_file, params=param_file_iec_101, data=payload, files=files_iec_101, verify=False)

    # IEC-104
    param_file_iec_104 = {"mid": "7f88b4b5-91dd-46e4-b443-99898902ef09", "sid": "null", "type": "DEV"}
    files_iec_104 = [(filetype, ('МЭК-104 v1.xml', open(path+'МЭК-104 v1.xml', 'rb'), 'text/xml'))]                                                                
    modbus_rtu = s.post(url_file, params=param_file_iec_104, data=payload, files=files_iec_104, verify=False)
    
    s.close()
