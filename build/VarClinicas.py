import requests
import csv
from secrets import credenciales
#!/usr/bin/env python
data = {
    'token': credenciales.get("SECRET_KEY"),
    'content': 'report',
    'format': 'csv',
    'report_id': '120',
    'csvDelimiter': '',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'false',
    'returnFormat': 'csv'
}
data = requests.post('https://redcap.infant.org.ar/es/api/',data=data)
lines = data.text.splitlines()
reader = csv.reader(lines)
for row in reader:
    with open('informes/VarClinicas.csv', 'w', newline='') as csvfile:
        spamwriter = csv.writer(csvfile,quotechar=',')
        for row in reader:
            spamwriter.writerow(row)  