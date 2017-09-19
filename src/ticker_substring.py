import csv
from  __builtin__ import any as b_any


done_file = open("/home/jay/Desktop/file_to_process_2.csv")
done_file_reader = csv.reader(done_file)
tickers = []
for row in done_file_reader:
    ticker = row[0]
    ticker = ticker.split(" ",1)[0]
    tickers.append(ticker)

print tickers

exampleFile = open('/home/jay/Pictures/bloomberg/effb9b35d00f0eb6.csv')

exampleReader = csv.reader(exampleFile)
company_i = []
companies_i = []
count = 1

for row in exampleReader:
    count = count + 1
    if row[2] == "2016":
        if b_any(row[7] in x for x in tickers):
            print "done" + row[7]
        else:
            if '.' not in row[7]:
                company_i.append(row[7])
                company_i.append(row[9])
                companies_i.append(company_i)
                company_i = []

comp = [list(item) for item in set(tuple(row) for row in companies_i)]


with open("/home/jay/Desktop/us_tickers.csv", 'wb') as myfile:
    writer = csv.writer(myfile)
    for val in comp:
        writer.writerow(val)




