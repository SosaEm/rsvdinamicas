import MySQLdb as db
import csv
from secrets import credenciales

def Query(tabla,query,archivo,head):
    # Correr query y guardarlo en `data`
    with db.connect(host="127.0.0.1",
                    user=credenciales.get("DATABASE_USER"),    
                    passwd=credenciales.get("DATABASE_PASSWORD"),
                    db= tabla) as conn:
        cur = conn.cursor()
        sql = query
        cur.execute(sql)
        data = cur.fetchall()
        cur.close() #Ver si hace falta cerrar la conexion

    # Crear csv
    with open("informes/" + str(archivo) + ".csv", 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        # Crear encabezado del csv
        header = [head]
        writer.writerow(header)
        # Copiar `data`  y escribir en el csv
        for row in data:
            writer.writerow(row)