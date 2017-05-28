from os import listdir
from os.path import isfile, join
import csv
from database import Database

def remove_spaces(str):
    count = str.count(" ")
    count = count - 1
    str_f = str.replace(" ", "", count)
    return str_f

db = Database()

onlyfiles = [f for f in listdir("/home/jay/Desktop/ocr_output/") if isfile(join("/home/jay/Desktop/ocr_output/", f))]

print onlyfiles

read_firstline = False

processed_firms = []

for filename in onlyfiles:
    with open("/home/jay/Desktop/ocr_output/"+filename) as fp:
        for line in fp:
            line = line.rstrip()
            if "jay" in line:
                image_path = line
                image = line.rsplit("/", 1)[1]
                print "Processing file %s" % image
                image_name = image
                read_firstline = True
            else:
                ticker_s = remove_spaces(line)
                if read_firstline:
                    print ticker_s
                    processed_firms.append(ticker_s)
                    read_firstline = False
                else:
                    print "nothing"

print processed_firms
processed_firms = sorted(set(processed_firms), key=processed_firms.index)
#processed_firms_list = list(processed_firms)

with open("/home/jay/Desktop/customer_list.csv", 'wb') as myfile:
    writer = csv.writer(myfile)
    for val in processed_firms:
        writer.writerow([val])

reader = csv.reader(open('/home/jay/Desktop/customer_list.csv', 'rb'))
writer = csv.writer(open('/home/jay/Desktop/customer_list_name.csv', 'w'))

for row in reader:
    print row[0]
    company = db.query("""select CompanyName from ticker_list where Ticker LIKE '{ticker}'""".format(ticker=row[0]))
    if len(company) > 0:
        company_name = company[0]['CompanyName']
    else:
        company_name = row[0]
    print company_name
    row.append(company_name)
    writer.writerow(row)
