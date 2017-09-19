from database import Database
import csv

db = Database()

insert_query = """
    INSERT INTO incorrect_ticker_list (Ticker, CompanyName, ImageName)
    VALUES ('{ticker}', '-', '{image_name}');
    """

select_query = """
        SELECT * FROM ticker_list where Ticker LIKE '{ticker}'
        """
select_iquery = """
        SELECT * FROM incorrect_ticker_list where Ticker LIKE '{ticker}'
        """

select_rquery = """
        SELECT * FROM re_ticker_list where Ticker LIKE '{ticker}'
        """

companies = db.query(select_query)

#for company in companies:
#    print "Found %s " % company['Ticker']

exampleFile = open('/home/jay/Desktop/customer_list_name.csv')

exampleReader = csv.reader(exampleFile)
check_list = []
done_list = []
count = 1

for row in exampleReader:

    count = count + 1

    companies = db.query(select_query.format(ticker=row[0]))
    in_companies = db.query(select_iquery.format(ticker=row[0]))
    re_companies = db.query(select_rquery.format(ticker=row[0]))
    if len(companies) > 0 or len(in_companies) > 0 or len(re_companies) > 0:
        if len(companies) > 0:
            done_list.append(companies[0]['id'])
            #print companies[0]['id']
        if len(in_companies) > 0:
            done_list.append(in_companies[0]['id'])
            #print in_companies[0]['id']
        if len(re_companies) > 0:
            done_list.append(re_companies[0]['id'])
            #print re_companies[0]['id']
    else:
        print companies
        print in_companies
        print re_companies
        print "check"
        print row[0]
        check_list.append(row[0])

    # if len(companies) == 0:
    #     db.insert(insert_query.format(ticker=row[0], image_name=row[1]))
    #     print('Row #' + str(exampleReader.line_num) + ' ' + str(row))
    # else:
    #     print "%s ticker already exists"%row[0]

print check_list
print len(check_list)

#print done_list
print sorted(done_list)
print len(done_list)