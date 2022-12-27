import MySQLdb as db
import csv
from secrets import credenciales

def NoHipox():
    # Correr query y guardarlo en `data`
    with db.connect(host="127.0.0.1",
                    user=credenciales.get("DATABASE_USER"),    
                    passwd=credenciales.get("DATABASE_PASSWORD"),
                    db="rsv dinamicas") as conn:
        cur = conn.cursor()
        sql = "SELECT record_id,hospital,hipox_taquipn,dx_respi___1,dx_respi___2,dx_respi___3,dx_respi___4,dx_respi___5,dx_respi___6,dx_respi___7,otro_dx,dx_respi___0,comentarios FROM rsvdinamicas WHERE hipox_taquipn!=1 AND dx_respi___5 !=1"
        cur.execute(sql)
        data = cur.fetchall()
        cur.close() #Ver si hace falta cerrar la conexion

    # Crear csv
    with open('informes/NoHipox.csv', 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        # Crear encabezado del csv
        header = ['Record_ID', 'hospital', 'hipox_taquipn', 'Bronquiolitis', 'Neumonia', 'Supuracion pleuropulmonar', 'Apneas', 'Sindrome Coqueluchoide', 'Sindrome broncoobstructivo', 'Otro', 'Otro diagnostico', 'Ns', 'Comentarios']
        writer.writerow(header)
        # Copiar `data`  y escribir en el csv
        for row in data:
            writer.writerow(row)