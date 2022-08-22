import MySQLdb as db
import csv
from secrets import credenciales

def CompletadoPor():
    # Correr query y guardarlo en `data`
    with db.connect(host="127.0.0.1",
                    user=credenciales.get("DATABASE_USER"),    
                    passwd=credenciales.get("DATABASE_PASSWORD"),
                    db="rsv dinamicas") as conn:
        cur = conn.cursor()
        sql = "SELECT a.formcomplete, (SELECT COUNT(*) FROM rsvdinamicas WHERE formcomplete = a.formcomplete) as TotalCount FROM (SELECT DISTINCT formcomplete FROM rsvdinamicas) a ;"
        cur.execute(sql)
        data = cur.fetchall()
        cur.close() #Ver si hace falta cerrar la conexion

    # Crear csv
    with open('informes/CompletadoPor.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        # Crear encabezado del csv
        header = ['Completado por', 'Total']
        writer.writerow(header)
        # Copiar `data`  y escribir en el csv
        for row in data:
            writer.writerow(row)