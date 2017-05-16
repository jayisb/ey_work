from database import Database
import csv

db = Database()

insert_query = """
    INSERT INTO incorrect_ticker_list (Ticker, CompanyName, ImageName)
    VALUES ('{ticker}', '-', '{image_name}');
    """

select_query = """
        SELECT * FROM incorrect_ticker_list where Ticker LIKE '{ticker}'
        """

companies = db.query(select_query)

#for company in companies:
#    print "Found %s " % company['Ticker']

exampleFile = open('/home/jay/Documents/nincorrect_kor.csv')

exampleReader = csv.reader(exampleFile)

for row in exampleReader:
    print row[0]
    print row[1]
    companies = db.query(select_query.format(ticker=row[0]))
    print companies
    if len(companies) == 0:
        db.insert(insert_query.format(ticker=row[0], image_name=row[1]))
        print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
    else:
        print "%s ticker already exists"%row[0]
