SELECT record_id,hospital,dx_respi___1,dx_respi___2,dx_respi___3,dx_respi___4,dx_respi___5,dx_respi___6,dx_respi___7,dx_respi___0 FROM rsvdinamicas WHERE dx_respi___1=0 and dx_respi___2=0 and dx_respi___3=0 and dx_respi___4=0 and dx_respi___5=0 and dx_respi___6=0 and dx_respi___7=0 and dx_respi___0=0;

SELECT record_id,hospital,hipox_taquipn FROM rsvdinamicas WHERE hipox_taquipn!=1


SELECT record_id,hospital,fecha_ingreso,fecha_de_nacimiento,@edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30  FROM rsvdinamicas WHERE @edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30>60 or @edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30<0


SELECT record_id,hospital,fecha_ingreso,fecha_alta_irab,@diasirab := (DATEDIFF(fecha_alta_irab,fecha_ingreso)) FROM rsvdinamicas WHERE @diasirab := (DATEDIFF(fecha_alta_irab,fecha_ingreso))<1 or @diasirab := (DATEDIFF(fecha_alta_irab,fecha_ingreso))>180

SELECT record_id,hospital FROM rsvdinamicas WHERE hospital=3

  #Cantidad de fichas cargadas por cada usuario#
SELECT a.formcomplete,
    (SELECT COUNT(*) FROM rsvdinamicas WHERE formcomplete = a.formcomplete) as TotalCount
FROM (SELECT DISTINCT formcomplete FROM rsvdinamicas) a ;


SELECT record_id,hospital,fecha_ingreso,formcomplete FROM rsvdinamicas WHERE record_id LIKE '%2018%' and fecha_ingreso NOT LIKE '%2018%';

SELECT record_id,hospital,fecha_ingreso,formcomplete FROM rsvdinamicas WHERE record_id LIKE '%2019%' and fecha_ingreso NOT LIKE '%2019%';

SELECT record_id,hospital,fecha_ingreso,formcomplete FROM rsvdinamicas WHERE record_id LIKE '%2020%' and fecha_ingreso NOT LIKE '%2020%';

SELECT record_id,hospital,fecha_ingreso,formcomplete FROM rsvdinamicas WHERE record_id LIKE '%2021%' and fecha_ingreso NOT LIKE '%2021%';

SELECT record_id,hospital,fecha_ingreso,formcomplete FROM rsvdinamicas WHERE record_id LIKE '%2022%' and fecha_ingreso NOT LIKE '%2022%';

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 1 and areaprog = 0) and (partido = 6 or partido = 4 or partido = 13 or partido = 38 or partido = 40 or partido = 41 or partido = 74 or partido = 67 or partido = 101 or partido = 14 or partido = 17 or partido = 19 or partido = 24 or partido = 26 or partido = 35 or partido = 36 or partido = 46 or partido = 52 or partido = 66 or partido = 76 or partido = 83 or partido = 95 or partido = 98 or partido = 100 or partido = 119 or partido = 124);

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 1 and areaprog = 1) and (partido != 6 and partido != 4 and partido != 13 and partido != 38 and partido != 40 and partido != 41 and partido != 74 and partido != 67 and partido != 101 and partido != 14 and partido != 17 and partido != 19 and partido != 24 and partido != 26 and partido != 35 and partido != 36 and partido != 46 and partido != 52 and partido != 66 and partido != 76 and partido != 83 and partido != 95 and partido != 98 and partido != 100 and partido != 119 and partido != 124);

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 3 and areaprog = 0) and (partido = 6 or partido = 4 or partido = 13 or partido = 38 or partido = 40 or partido = 41 or partido = 74 or partido = 67 or partido = 101);

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 3 and areaprog = 1) and (partido != 6 and partido != 4 and partido != 13 and partido != 38 and partido != 40 and partido != 41 and partido != 74 and partido != 67 and partido != 101);

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 4 and areaprog = 0) and (partido = 6 or partido = 4 or partido = 13 or partido = 38 or partido = 40 or partido = 41 or partido = 74 or partido = 67 or partido = 101 or partido = 135);

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 4 and areaprog = 1) and (partido != 6 and partido != 4 and partido != 13 and partido != 38 and partido != 40 and partido != 41 and partido != 74 and partido != 67 and partido != 101 and partido != 135);

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 5 and areaprog = 0) and (partido = 49 or partido = 55 or partido = 61 or partido = 62 or partido = 75 or partido = 80 or partido = 82 or partido = 85 or partido = 86 or partido = 128 or partido = 65);

SELECT record_id,hospital,areaprog,partido FROM rsvdinamicas WHERE (hospital = 5 and areaprog = 1) and (partido != 49 and partido != 55 and partido != 61 and partido != 62 and partido != 75 and partido != 80 and partido != 82 and partido != 85 and partido != 86 and partido != 128 and partido != 65);

SELECT record_id,hospital FROM rsvdinamicas WHERE complicaciones___0 = 0 AND complicaciones___1 = 0 AND complicaciones___2 = 0 AND complicaciones___3 = 0 AND complicaciones___4 = 0 AND complicaciones___5 = 0 AND complicaciones___6 = 0 AND complicaciones___7 = 0 AND complicaciones___8 = 0 AND complicaciones___9 = 0 AND complicaciones___10 = 0 AND complicaciones___11 = 0;

select record_id,edad_gest from rsvdinamicas where edad_gest >45 or edad_gest <20;