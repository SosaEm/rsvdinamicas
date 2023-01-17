select SUBSTRING(record_id,1,7),count(*) from rsvdinamicas group by 1 having count(*)>1 

select record_id,fecha_de_nacimiento from rsvdinamicas where SUBSTRING(record_id,1,7) 

SELECT SUBSTR(record_id, 1, 7) AS prefix FROM rsvdinamicas
GROUP BY prefix
HAVING COUNT(DISTINCT record_id) > 2
