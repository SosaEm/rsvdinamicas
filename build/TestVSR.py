from getpass import getpass
import MySQLdb as db
import csv

# Correr query y guardarlo en `data`
with db.connect(host="127.0.0.1",
                user=input("User: "),    
                passwd=getpass("Pass: "),
                db="rsv dinamicas") as conn:
    cur = conn.cursor()
    sql = "SELECT record_id,hospital,test_vsr FROM rsvdinamicas WHERE test_vsr!=1"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close() #Ver si hace falta cerrar la conexion

# Crear csv
with open('informes/TestVSR.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Crear encabezado del csv
    header = ['ID', 'hospital', 'Test VSR']
    writer.writerow(header)
    # Copiar `data`  y escribir en el csv
    for row in data:
        writer.writerow(row)