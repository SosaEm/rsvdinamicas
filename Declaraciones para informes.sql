SELECT record_id,hospital,dx_respi___1,dx_respi___2,dx_respi___3,dx_respi___4,dx_respi___5,dx_respi___6,dx_respi___7,dx_respi___0 FROM rsvdinamicas WHERE dx_respi___1=0 and dx_respi___2=0 and dx_respi___3=0 and dx_respi___4=0 and dx_respi___5=0 and dx_respi___6=0 and dx_respi___7=0 and dx_respi___0=0;

SELECT record_id,hospital,hipox_taquipn FROM rsvdinamicas WHERE hipox_taquipn!=1


SELECT record_id,hospital,fecha_ingreso,fecha_de_nacimiento,@edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30  FROM rsvdinamicas WHERE @edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30>60 or @edadmeses := (DATEDIFF(fecha_ingreso,fecha_de_nacimiento))/30<0


SELECT record_id,hospital,fecha_ingreso,fecha_alta_irab,@diasirab := (DATEDIFF(fecha_alta_irab,fecha_ingreso)) FROM rsvdinamicas WHERE @diasirab := (DATEDIFF(fecha_alta_irab,fecha_ingreso))<1 or @diasirab := (DATEDIFF(fecha_alta_irab,fecha_ingreso))>180

SELECT record_id,hospital FROM rsvdinamicas WHERE hospital=3

  #Cantidad de fichas cargadas por cada usuario#
SELECT a.formcomplete,
    (SELECT COUNT(*) FROM rsvdinamicas WHERE formcomplete = a.formcomplete) as TotalCount
FROM (SELECT DISTINCT formcomplete FROM rsvdinamicas) a ;