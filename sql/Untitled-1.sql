SELECT * FROM rsvdinmicascovid19ga


SELECT * FROM rsvdinmicascovid19ga WHERE hospital=3
INTO OUTFILE "C:/Users/esosa/Desktop/LUDOVICA.csv"
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'; 

SELECT record_id,hospital,hipox_taquipn FROM rsvdinmicascovid19ga WHERE hipox_taquipn!=1
INTO OUTFILE "C:/Users/esosa/Desktop/NoHipox.csv"
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'; 

SHOW PROCESSLIST
select @@max_allowed_packet;
set global max_allowed_packet=10485760;

SELECT * FROM rsvdinamicas

SELECT COUNT(*) FROM rsvdinamicas