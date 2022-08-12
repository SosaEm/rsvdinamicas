#!/usr/bin/env python
import json
import requests
data = {
    'token': 'BE6F7745D6368829E2804EC191EC6799',
    'content': 'report',
    'format': 'json',
    'report_id': '114',
    'csvDelimiter': '',
    'rawOrLabel': 'label',
    'rawOrLabelHeaders': 'label',
    'exportCheckboxLabel': 'true',
    'returnFormat': 'json'
}
r = requests.post('https://redcap.infant.org.ar/es/api/',data=data)
r.json()
print('HTTP Status: ' + str(r.status_code))

with open('informes/personal.json', 'w') as json_file:
    json.dump(r.json(), json_file)
