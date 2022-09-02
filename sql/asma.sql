select p.*
from controles p join
     (select codigo_id, max(fecha) as maxid
      from controles
      group by codigo_id
     ) pmax
     on p.fecha = pmax.maxid;



select controles.codigo_id, epi.codigo_id, max(controles.fecha)
from controles
join epi
on controles.codigo_id = epi.codigo_id
group by epi.codigo_id

SELECT codigo_id, fecha
FROM controles AS a
WHERE fecha = (
    SELECT max(fecha)
    FROM controles AS b
    WHERE a.codigo_id = b.codigo_id
)
