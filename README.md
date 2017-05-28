# ey_work
6206

select Ticker, CompanyName from ticker_list where id > 4070 ORDER BY id
INTO OUTFILE '/var/lib/mysql-files/file_to_process_27.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';