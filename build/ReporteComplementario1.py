import csv
import MySQLdb as db
from secrets import credenciales

database_name = "rsv dinamicas"

def run_query(sql):
    with db.connect(host="127.0.0.1",
                    user=credenciales.get("DATABASE_USER"),
                    passwd=credenciales.get("DATABASE_PASSWORD"),
                    db=database_name) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        cur.close()
    return data

def write_to_csv(file_path, header, data):
    with open(file_path, 'w', newline='') as f_handle:
        writer = csv.writer(f_handle)
        writer.writerow(header)
        writer.writerows(data)

# Query 1
sql = "SELECT record_id,hospital,fecha_in_uti,fecha_eg_uti,@diasuti := (DATEDIFF(fecha_eg_uti, 	fecha_in_uti)),comentarios,formcomplete FROM rsvdinamicas WHERE @diasuti := (DATEDIFF(fecha_eg_uti,fecha_in_uti))<1 or @diasirab := (DATEDIFF(fecha_eg_uti,fecha_in_uti))>180"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'fecha de ingreso uti', 'fecha de alta uti', 'dias uti', 'Comentarios', 'Completado por']
write_to_csv('informes/DiasUTI.csv', header, data)

# Query 2
sql = "SELECT record_id,hospital,uti,comentarios,formcomplete FROM rsvdinamicas WHERE uti is NULL"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'uti', 'Comentarios', 'Completado por']
write_to_csv('informes/UTI.csv', header, data)

# Query 3
sql = "SELECT record_id,hospital,uti,fecha_in_uti,fecha_eg_uti,comentarios,formcomplete FROM rsvdinamicas WHERE uti = 1 AND fecha_alta_irab IS NOT NULL AND (fecha_in_uti IS NULL OR fecha_eg_uti IS NULL)"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'uti', 'fecha ingreso uti', 'fecha egreso uti', 'Comentarios', 'Completado por']
write_to_csv('informes/UTIMVS.csv', header, data)

# Query 4
sql = "select record_id,hospital,edad_gest,comentarios,formcomplete from rsvdinamicas where edad_gest >45 or edad_gest <20;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'edad gestacional', 'Comentarios', 'Completado por']
write_to_csv('informes/EdadGest.csv', header, data)

# Query 5
sql = "select record_id,hospital,tecnica_vsr1,comentarios,formcomplete from rsvdinamicas where tecnica_vsr1 is NULL AND resultado_vsr1=1;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'tecnica vsr', 'Comentarios', 'Completado por']
write_to_csv('informes/TecnicaVSR.csv', header, data)

# Query 6
sql = "select record_id,hospital,cultivo_at,resultado_at___0, resultado_at___1, resultado_at___2, resultado_at___3, resultado_at___4, resultado_at___5, resultado_at___6, resultado_at___7, resultado_at___8, resultado_at___9, resultado_at___10, resultado_at___11, resultado_at___12, resultado_at___13,comentarios,formcomplete from rsvdinamicas where resultado_at___0=0 AND resultado_at___1=0 AND resultado_at___2=0 AND resultado_at___3=0 AND resultado_at___4=0 AND resultado_at___5=0 AND resultado_at___6=0 AND resultado_at___7=0 AND resultado_at___8=0 AND resultado_at___9=0 AND resultado_at___10=0 AND resultado_at___11=0 AND resultado_at___12=0 AND resultado_at___13=0 AND cultivo_at =1;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'cultivo_at', 'resultado_at___0', 'resultado_at___1', 'resultado_at___2', 'resultado_at___3', 'resultado_at___4', 'resultado_at___5', 'resultado_at___6', 'resultado_at___7', 'resultado_at___8', 'resultado_at___9', 'resultado_at___10', 'resultado_at___11', 'resultado_at___12', 'resultado_at___13', 'Comentarios', 'Completado por']
write_to_csv('informes/AspTraqueal.csv', header, data)

# Query 7
sql = "select record_id,hospital,test_covid,resultado_covid,comentarios,formcomplete from rsvdinamicas where test_covid =1 AND resultado_covid IS NULL;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'test_covid', 'resultado_covid','Comentarios', 'Completado por']
write_to_csv('informes/ResCOVID.csv', header, data)

# Query 8
sql = "select record_id,hospital,hmc,resultado_hmc___0, resultado_hmc___1, resultado_hmc___2, resultado_hmc___3, resultado_hmc___4, resultado_hmc___5, resultado_hmc___6, resultado_hmc___7, resultado_hmc___8, comentarios,formcomplete from rsvdinamicas where resultado_hmc___0=0 AND resultado_hmc___1=0 AND resultado_hmc___2=0 AND resultado_hmc___3=0 AND resultado_hmc___4=0 AND resultado_hmc___5=0 AND resultado_hmc___6=0 AND resultado_hmc___7=0 AND resultado_hmc___8=0 AND hmc =1;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'hmc', 'resultado_hmc___0', 'resultado_hmc___1', 'resultado_hmc___2', 'resultado_hmc___3', 'resultado_hmc___4', 'resultado_hmc___5', 'resultado_hmc___6', 'resultado_hmc___7', 'resultado_hmc___8', 'Comentarios', 'Completado por']
write_to_csv('informes/HMC.csv', header, data)

# Query 9
sql = "select record_id,hospital,cultivo_pleural,resultado_liqpleural___0, resultado_liqpleural___1, resultado_liqpleural___2, resultado_liqpleural___3, resultado_liqpleural___4, resultado_liqpleural___5, resultado_liqpleural___6, resultado_liqpleural___7, resultado_liqpleural___8, comentarios,formcomplete from rsvdinamicas where resultado_liqpleural___0=0 AND resultado_liqpleural___1=0 AND resultado_liqpleural___2=0 AND resultado_liqpleural___3=0 AND resultado_liqpleural___4=0 AND resultado_liqpleural___5=0 AND resultado_liqpleural___6=0 AND resultado_liqpleural___7=0 AND resultado_liqpleural___8=0 AND cultivo_pleural =1;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'cultivo_pleural', 'resultado_liqpleural___0', 'resultado_liqpleural___1', 'resultado_liqpleural___2', 'resultado_liqpleural___3', 'resultado_liqpleural___4', 'resultado_liqpleural___5', 'resultado_liqpleural___6', 'resultado_liqpleural___7', 'resultado_liqpleural___8', 'Comentarios', 'Completado por']
write_to_csv('informes/LiqPleural.csv', header, data)

# Query 10
sql = "select record_id,hospital,test_bordetella,resultado_bordetella,comentarios,formcomplete from rsvdinamicas where test_bordetella =1 AND resultado_bordetella IS NULL;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'test_bordetella', 'resultado_bordetella','Comentarios', 'Completado por']
write_to_csv('informes/ResBordetella.csv', header, data)

# Query 11
sql = "select record_id,hospital,test_viro,resultado_viro___0, resultado_viro___1, resultado_viro___2, resultado_viro___3, resultado_viro___4, resultado_viro___5, resultado_viro___6, comentarios,formcomplete from rsvdinamicas where resultado_viro___0=0 AND resultado_viro___1=0 AND resultado_viro___2=0 AND resultado_viro___3=0 AND resultado_viro___4=0 AND resultado_viro___5=0 AND resultado_viro___6=0 AND test_viro =1;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'cultivo_pleural', 'resultado_viro___0', 'resultado_viro___1', 'resultado_viro___2', 'resultado_viro___3', 'resultado_viro___4', 'resultado_viro___5', 'resultado_viro___6',  'Comentarios', 'Completado por']
write_to_csv('informes/OtrosVirus.csv', header, data)

# Query 12
sql = "select record_id,hospital,test_vsr,resultado_vsr1,comentarios,formcomplete from rsvdinamicas where test_vsr =1 AND resultado_vsr1 IS NULL;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'test_vsr', 'resultado_vsr','Comentarios', 'Completado por']
write_to_csv('informes/ResVSR.csv', header, data)

# Query 13
sql = "SELECT record_id,hospital,comorbilidades___0,comorbilidades___1,comorbilidades___2,comorbilidades___3,comorbilidades___4,comorbilidades___5,comorbilidades___6,comorbilidades___7,comorbilidades___8,comorbilidades___9,comorbilidades___10,comorbilidades___11,comorbilidades___12,comorbilidades___13,comorbilidades___14,comentarios,formcomplete FROM rsvdinamicas WHERE comorbilidades___0 = 0 AND comorbilidades___1 = 0 AND comorbilidades___2 = 0 AND comorbilidades___3 = 0 AND comorbilidades___4 = 0 AND comorbilidades___5 = 0 AND comorbilidades___6 = 0 AND comorbilidades___7 = 0 AND comorbilidades___8 = 0 AND comorbilidades___9 = 0 AND comorbilidades___10 = 0 AND comorbilidades___11 = 0 AND comorbilidades___12 = 0 AND comorbilidades___13 = 0 AND comorbilidades___14 = 0;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'comorbilidades___0' , 'comorbilidades___1' , 'comorbilidades___2' , 'comorbilidades___3' , 'comorbilidades___4' , 'comorbilidades___5' , 'comorbilidades___6' , 'comorbilidades___7' , 'comorbilidades___8' , 'comorbilidades___9' , 'comorbilidades___10' , 'comorbilidades___11' , 'comorbilidades___12' , 'comorbilidades___13' , 'comorbilidades___14' , 'Comentarios', 'Completado por']
write_to_csv('informes/Comorbilidades.csv', header, data)

# Query 14
sql = "SELECT record_id,hospital,complicaciones___0,complicaciones___1,complicaciones___2,complicaciones___3,complicaciones___4,complicaciones___5,complicaciones___6,complicaciones___7,complicaciones___8,complicaciones___9,complicaciones___10,complicaciones___11,comentarios,formcomplete FROM rsvdinamicas WHERE complicaciones___0 = 0 AND complicaciones___1 = 0 AND complicaciones___2 = 0 AND complicaciones___3 = 0 AND complicaciones___4 = 0 AND complicaciones___5 = 0 AND complicaciones___6 = 0 AND complicaciones___7 = 0 AND complicaciones___8 = 0 AND complicaciones___9 = 0 AND complicaciones___10 = 0 AND complicaciones___11 = 0 AND fecha_alta_irab IS NOT NULL;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'complicaciones___0' , 'complicaciones___1' , 'complicaciones___2' , 'complicaciones___3' , 'complicaciones___4' , 'complicaciones___5' , 'complicaciones___6' , 'complicaciones___7' , 'complicaciones___8' , 'complicaciones___9' , 'complicaciones___10' , 'complicaciones___11' ,  'Comentarios', 'Completado por']
write_to_csv('informes/Complicaciones.csv', header, data)

# Query 15
sql = "SELECT record_id,hospital,sx_ingreso___0,sx_ingreso___1,sx_ingreso___2,sx_ingreso___3,sx_ingreso___4,sx_ingreso___5,sx_ingreso___6,sx_ingreso___7,sx_ingreso___8,sx_ingreso___9,comentarios,formcomplete FROM rsvdinamicas WHERE sx_ingreso___0 = 0 AND sx_ingreso___1 = 0 AND sx_ingreso___2 = 0 AND sx_ingreso___3 = 0 AND sx_ingreso___4 = 0 AND sx_ingreso___5 = 0 AND sx_ingreso___6 = 0 AND sx_ingreso___7 = 0 AND sx_ingreso___8 = 0 AND sx_ingreso___9 = 0;"
data = run_query(sql)
header = ['Record_ID', 'hospital', 'sx_ingreso___0' , 'sx_ingreso___1' , 'sx_ingreso___2' , 'sx_ingreso___3' , 'sx_ingreso___4' , 'sx_ingreso___5' , 'sx_ingreso___6' , 'sx_ingreso___7' , 'sx_ingreso___8' , 'sx_ingreso___9' ,  'Comentarios', 'Completado por']
write_to_csv('informes/Sx_Ingreso.csv', header, data)

# Query 16
sql = "SELECT record_id,hospital,dispositivo_o2___1,dispositivo_o2___2,dispositivo_o2___3,dispositivo_o2___4,dispositivo_o2___5,dispositivo_o2___6,comentarios,formcomplete FROM rsvdinamicas WHERE dispositivo_o2___1 = 0 AND dispositivo_o2___2 = 0 AND dispositivo_o2___3 = 0 AND dispositivo_o2___4 = 0 AND dispositivo_o2___5 = 0 AND dispositivo_o2___6 = 0;"
data = run_query(sql)
header = ['Record_ID', 'hospital',  'dispositivo_o2___1' , 'dispositivo_o2___2' , 'dispositivo_o2___3' , 'dispositivo_o2___4' , 'dispositivo_o2___5' , 'dispositivo_o2___6' , 'Comentarios', 'Completado por']
write_to_csv('informes/DispO2.csv', header, data)

# Query 17
sql = "SELECT record_id,hospital,sexo,comentarios,formcomplete FROM rsvdinamicas WHERE sexo IS NULL;"
data = run_query(sql)
header = ['Record_ID', 'hospital',  'sexo' ,  'Comentarios', 'Completado por']
write_to_csv('informes/Sexo.csv', header, data)

# Query 18
sql = "SELECT record_id,hospital,cobertura,comentarios,formcomplete FROM rsvdinamicas WHERE cobertura IS NULL;"
data = run_query(sql)
header = ['Record_ID', 'hospital',  'cobertura' ,  'Comentarios', 'Completado por']
write_to_csv('informes/Cobertura.csv', header, data)