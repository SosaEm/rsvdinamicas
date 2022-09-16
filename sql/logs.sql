select usuario, @semana:=(week(tiempo)) from logs
SELECT week(tiempo),usuario,count(week(tiempo)) from logs where usuario ="gsanluis" group by week(tiempo)

SELECT week(tiempo),usuario,count(week(tiempo)) from logs group by week(tiempo),usuario order by usuario,week(tiempo)
