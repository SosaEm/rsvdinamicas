import requests
import csv
#!/usr/bin/env python
data = {
    'token': 'BE6F7745D6368829E2804EC191EC6799',
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