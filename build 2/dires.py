import json
import requests
import csv
from pwd import credenciales

data = {
    'token': credenciales.get("SECRET_KEY"),
    'content': 'report',
    'format': 'csv',
    'report_id': '114',
    'csvDelimiter': '',
    'rawOrLabel': 'raw',
    'rawOrLabelHeaders': 'raw',
    'exportCheckboxLabel': 'true',
    'returnFormat': 'json'
}
data = requests.post('https://redcap.infant.org.ar/es/api/',data=data)
lines = data.text.splitlines()
reader = csv.reader(lines)
for row in reader:
    with open('build 2/dire.csv', 'w', newline='', encoding='utf-8') as csvfile:
        spamwriter = csv.writer(csvfile,quotechar=',')
        for row in reader:
            spamwriter.writerow(row)  