select COUNT(*) from (SELECT COUNT(*) from path where s6 = 2 group by codigo_id) AS grp

SELECT codigo_id,COUNT(*) from path where redcap_event_name IS NOT NULL group by codigo_id

SELECT codigo_id,@sibilante := IF ((SELECT COUNT(*) from path where evento IS NOT NULL) =1,0,1) as sibilante from path group by codigo_id

select codigo_id,e5_8 from path where e5_8 is not null group by codigo_id

select count(*) from path where e5_8 not like "" AND event like "base_arm_1"

SELECT codigo_id,@sibilante := CASE WHEN (SELECT codigo_id,COUNT(*) from path where evento IS NOT NULL group by codigo_id) =1 AND evento LIKE "base_arm_1" THEN 0 ELSE 1 END as sibilante from path group by codigo_id

SELECT codigo_id, CASE WHEN (SELECT COUNT(*) from path where evento IS NOT NULL) =1 AND evento LIKE "base_arm_1" THEN 0 ELSE 1 END as sibilante from path group by codigo_id

SELECT codigo_id, CASE WHEN (SELECT COUNT(codigo_id) from path group by codigo_id) >1 THEN 1 ELSE 0 END as sibilante from path group by codigo_id

SELECT COUNT(codigo_id) from path group by codigo_id

BEGIN
WHILE (SELECT COUNT(codigo_id) from path group by codigo_id) >1 AND evento LIKE "base_arm_1" from path DO;
    SET sibilante = 1;
END WHILE;
END;

IF ((SELECT COUNT(codigo_id) from path group by codigo_id) >1) AND (evento LIKE "base_arm_1" from path) THEN SET sibilante = 1
ELSE sibilante=0 from path

select codigo_id,count(codigo_id),@sibilante :=1 as sibilante from path group by codigo_id having count(codigo_id) >1


SELECT codigo_id
FROM path
WHERE codigo_id IN (
    SELECT codigo_id
    FROM path
    GROUP BY codigo_id
    HAVING COUNT(distinct evento) > 1
) group by codigo_id

SELECT codigo_id
FROM path
WHERE codigo_id IN (
    SELECT codigo_id
    FROM path
    GROUP BY codigo_id
    HAVING COUNT(distinct evento) = 1
) group by codigo_id