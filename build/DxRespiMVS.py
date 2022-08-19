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
    sql = "SELECT record_id,hospital,dx_respi___1,dx_respi___2,dx_respi___3,dx_respi___4,dx_respi___5,dx_respi___6,dx_respi___7,dx_respi___0 FROM rsvdinamicas WHERE dx_respi___1=0 and dx_respi___2=0 and dx_respi___3=0 and dx_respi___4=0 and dx_respi___5=0 and dx_respi___6=0 and dx_respi___7=0 and dx_respi___0=0;"
    cur.execute(sql)
    data = cur.fetchall()
    cur.close() #Ver si hace falta cerrar la conexion

# Crear csv
with open('informes/DxRespiMVS.csv', 'w', newline='') as f_handle:
    writer = csv.writer(f_handle)
    # Crear encabezado del csv
    header = ['Record_ID', 'hospital', 'dx_respi___1', 'dx_respi___2', 'dx_respi___3', 'dx_respi___4', 'dx_respi___5', 'dx_respi___6', 'dx_respi___7', 'dx_respi___0']
    writer.writerow(header)
    # Copiar `data`  y escribir en el csv
    for row in data:
        writer.writerow(row)