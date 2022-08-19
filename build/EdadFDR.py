from getpass import getpass
import MySQLdb as db
import csv
from secrets import credenciales

# Correr query y guardarlo en `data`
with db.connect(host="127.0.0.1",
                user=credenciales.get("DATABASE_USER"),    
                passwd=credenciales.get("DATABASE_PASSWORD"),
                db="rsv dinamicas") as conn:
    cur = conn.cursor()
    sql = "SELECT record_id,hospital,fecha_ingreso,fecha_de_nacimiento,@edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30  FROM rsvdinamicas WHERE @edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30>60 or @edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30<0"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close() #Ver si hace falta cerrar la conexion

# Crear csv
with open('informes/EdadFDR.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Crear encabezado del csv
    header = ['Record_ID', 'hospital', 'fecha de ingreso', 'fecha de nacimiento', 'edad en meses']
    writer.writerow(header)
    # Copiar `data`  y escribir en el csv
    for row in data:
        writer.writerow(row)