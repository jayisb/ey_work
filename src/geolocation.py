import csv

ticker_file = open("/home/jay/Desktop/china_tickers.csv")
ticker_file_reader = csv.reader(ticker_file)
tickers = []
single_row = []
rows = []
address_f = "=BDS(\"{ticker} Equity\",\"COMPANY_ADDRESS\",\"cols=1;rows=3\")"

for row in ticker_file_reader:
    print row[0]
    ticker = row[0]
    c_name = row[1]
    single_row.append(ticker)
    single_row.append(c_name)
    single_row.append(address_f.format(ticker=ticker))
    rows.append(single_row)
    single_row = []


with open("/home/jay/Desktop/china_tickers_g.csv", 'wb') as myfile:
    writer = csv.writer(myfile)
    for val in rows:
        writer.writerow(val)
        writer.writerow([])
        writer.writerow([])
        writer.writerow([])