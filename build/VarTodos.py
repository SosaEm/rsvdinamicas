#!/usr/bin/env python
import requests
import csv
from secrets import credenciales

def VarTodos():
    data = {
        'token': credenciales.get("SECRET_KEY"),
        'content': 'report',
        'format': 'csv',
        'report_id': '122',
        'csvDelimiter': ';',
        'rawOrLabel': 'raw',
        'rawOrLabelHeaders': 'raw',
        'exportCheckboxLabel': 'true',
        'returnFormat': 'csv'
    }
    r = requests.post('https://redcap.infant.org.ar/es/api/',data=data)
    print('HTTP Status: ' + str(r.status_code))
    lines = r.text.splitlines()
    reader = csv.reader(lines)
    for row in reader:
        with open('informes/TodosLosDatos.csv', 'w', newline='', encoding="utf-8") as csvfile:
            spamwriter = csv.writer(csvfile,quotechar=',')
            for row in reader:
                spamwriter.writerow(row)  
    return 'Archivo VarTodos.csv creado'