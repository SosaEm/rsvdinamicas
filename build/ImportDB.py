import MySQLdb as db
import csv
from secrets import credenciales


def importarbase():
    with db.connect(host="127.0.0.1",
                    user=credenciales.get("DATABASE_USER"),    
                    passwd=credenciales.get("DATABASE_PASSWORD"),
                    db="rsv dinamicas") as conn:
        cur = conn.cursor()
        tbl = 'rsvdinamicas'.split('.')[0]
        cnt = 0
        with open ('informes/TodosLosDatos.csv', 'r') as f:
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
