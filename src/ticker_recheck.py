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

ticker_check_query = """
                SELECT * FROM {table_name} where Ticker LIKE '{ticker}'"""

onlyfiles = [f for f in listdir("/home/jay/Desktop/ocr_output/") if isfile(join("/home/jay/Desktop/ocr_output/", f))]

print onlyfiles

read_firstline = False

processed_firms = []

onlyfiles = ['output_Ticker_25-05-2017.txt']
kaka_ni_tal = 0
to_be_added = set()

for filename in onlyfiles:
    with open("/home/jay/Desktop/ocr_output/"+filename) as fp:
        for line in fp:
            line = line.rstrip()
            if "jay" in line:
                image_path = line
                image = line.rsplit("/", 1)[1]
                #print "Processing file %s" % image
                image_name = image
                read_firstline = True
            else:
                ticker_s = remove_spaces(line)
                print ticker_s
                companies = db.query(ticker_check_query.format(table_name='ticker_list', ticker=ticker_s))
                invalid_companies = db.query(
                    ticker_check_query.format(table_name='incorrect_ticker_list', ticker=ticker_s))
                re_companies = db.query(ticker_check_query.format(table_name='re_ticker_list', ticker=ticker_s))
                #if len(companies) > 0 or len(invalid_companies) > 0:
                if len(companies) > 0 or len(invalid_companies) > 0 or len(re_companies) > 0:
                    kaka_ni_tal = 1
                    #print "%s ticker already exists" % ticker_s
                else:
                    print "Processing file %s" % image_name
                    to_be_added.add(ticker_s)
                    print "check %s"%ticker_s

print to_be_added