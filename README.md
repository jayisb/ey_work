# ey_work
6230

select Ticker, CompanyName from ticker_list where id > 4070 ORDER BY id
INTO OUTFILE '/var/lib/mysql-files/file_to_process_27.csv'
FIELDS TERMINATED BY ','
ENCLOSED BY '"'
LINES TERMINATED BY '\n';

6206 | WIL IN -> file_27
4070 | 3719 JP -> file_25

