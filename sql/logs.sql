SELECT year(tiempo) as 'anio', week(tiempo) as 'semana',usuario,count(week(tiempo)) as 'fichas cargadas' from logs WHERE year(tiempo) = 2023 group by week(tiempo),usuario order by usuario,week(tiempo)

select usuario, date(tiempo), min(tiempo) first, max(tiempo) last, TIMEDIFF(max(tiempo) , min(tiempo) ) as horas 
from logs
group by usuario, date(tiempo)