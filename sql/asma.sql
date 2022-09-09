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


select codigo_id,max(fecha) 
from (select max(fecha) as fecha from epi
union
select max(fecha) as fecha from inter);

select u.codigo_id
     , greatest(u.fecha,max(s.fecha),max(d.fecha),max(e.fecha))
  from epi u
     , inter s
     , clinica d
     , controles e             
 where s.codigo_id = u.codigo_id
 group by u.codigo_id
     , u.codigo_id
     , u.fecha