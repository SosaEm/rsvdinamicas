SELECT week(tiempo) as nSemana ,usuario,count(week(tiempo)) as cantidad from logs group by week(tiempo),usuario order by usuario,week(tiempo)

select '2018' as Anio, formcomplete, count(record_id) from rsvdinamicas where record_id like "%2018%" group by formcomplete

select '2019' as Anio, formcomplete, count(record_id) from rsvdinamicas where record_id like "%2019%" group by formcomplete

select '2020' as Anio, formcomplete, count(record_id) from rsvdinamicas where record_id like "%2020%" group by formcomplete

select '2021' as Anio, formcomplete, count(record_id) from rsvdinamicas where record_id like "%2021%" group by formcomplete

select '2022' as Anio, formcomplete, count(record_id) from rsvdinamicas where record_id like "%2022%" group by formcomplete

select '2018' as Anio, formcomplete, count(year(fecha_ingreso)) from rsvdinamicas where record_id like "%2018%" group by formcomplete

select record_id,formcomplete,hospital from rsvdinamicas where fecha_ingreso like "2018%"

SELECT record_id,hospital,fecha_ingreso FROM rsvdinamicas WHERE record_id LIKE '%2018%' and fecha_ingreso NOT LIKE '%2018%';

SELECT record_id,hospital,fecha_ingreso FROM rsvdinamicas WHERE record_id LIKE '%2019%' and fecha_ingreso NOT LIKE '%2019%';

SELECT record_id,hospital,fecha_ingreso FROM rsvdinamicas WHERE record_id LIKE '%2020%' and fecha_ingreso NOT LIKE '%2020%';

SELECT record_id,hospital,fecha_ingreso FROM rsvdinamicas WHERE record_id LIKE '%2021%' and fecha_ingreso NOT LIKE '%2021%';

SELECT record_id,hospital,fecha_ingreso FROM rsvdinamicas WHERE record_id LIKE '%2022%' and fecha_ingreso NOT LIKE '%2022%';