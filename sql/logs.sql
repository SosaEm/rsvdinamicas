select usuario, @semana:=(week(tiempo)) from logs
SELECT usuario,count(*) from logs where @semana:=(week(tiempo))=37


