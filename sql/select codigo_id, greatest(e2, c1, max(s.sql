select codigo_id, greatest(e2, c1, max(s_11), max(i_2), max(st_fechacontacto)) from fechas group by codigo_id
INTO OUTFILE "C:/Users/esosa/Desktop/probando.csv"
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'; 
