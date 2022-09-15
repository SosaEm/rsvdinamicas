#!/usr/bin/env python
import csv
import requests
import json
import MySQLdb as db
from secrets import credenciales

data = {
        'token': credenciales.get("SECRET_KEY"),
        'content': 'log',
        'logtype': 'record_add',
        'user': '',
        'record': '',
        'beginTime': '2022-01-10 22:27',
        'endTime': '',
        'format': 'json',
        'returnFormat': 'json'
    }
r = requests.post('https://redcap.infant.org.ar/es/api/',data=data)
r.json()
print('HTTP Status: ' + str(r.status_code))

with open('informes/log.json', 'w') as json_file:
    json.dump(r.json(), json_file)  


f = open(r'C:\Users\esosa\Desktop\Nominatim\rsvdinamicas\informes\log.json')
data=json.load(f)
json_str = json.dumps(data)
resp = json.loads(json_str)


with open('informes/log.json', 'r', encoding='utf-8') as json_file:
    for x in resp:
        id=(x['timestamp'])
        user=(x['username'])
        with open('informes/logs.csv', 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile)
            spamwriter.writerow(["{};{}" .format(id,user)])
           

with db.connect(host="127.0.0.1",
                    user=credenciales.get("DATABASE_USER"),    
                    passwd=credenciales.get("DATABASE_PASSWORD"),
                    db="rsv dinamicas") as conn:
        cur = conn.cursor()
        tbl = 'logs'.split('.')[0]
        cnt = 0
        with open ('informes/logs.csv', 'r') as f:
            reader = csv.reader(f, delimiter=';')
            for row in reader:
                #row.pop() # can be commented out
                row = ['NULL' if val == '' else val for val in row]
                row = [x.replace("'", "''") for x in row]
                out = "'" + "', '".join(item for item in row) + "'"
                out = out.replace("'NULL'", 'NULL')
                query = "REPLACE INTO " + tbl + " VALUES (" + out + ")"
                cur.execute(query)
                cnt = cnt + 1
                if cnt % 10000 == 0:
                    cur.commit()
            conn.commit()
        print("Uploaded " + str(cnt) + " rows into table " + tbl + ".")


