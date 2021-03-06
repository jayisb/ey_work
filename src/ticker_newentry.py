from bs4 import BeautifulSoup
import requests
import csv
from database import Database


def last_replace(s, old=" ", new=":", occurrence=1):
    li = s.rsplit(old, occurrence)
    return new.join(li)


def remove_spaces(str):
    count = str.count(" ")
    count = count - 1
    str_f = str.replace(" ", "", count)
    return str_f


def check_ticker(soup, ticker_c):
    tables = soup.findAll("table", {"class": "dual_border_data_table"})
    company_name = ""
    if len(tables) > 0:
        bm_table = tables[0]
        rows = bm_table.findAll("tr")
        row = rows[1]
        cells = row.findAll("td")
        if cells[0].get_text() == ticker_c:
            cn = cells[1].get_text()
            company_name = cn
        else:
            company_name = ""
            # print cn
    else:
        b = soup.findAll("div", {"class": "ticker_nomatches"})
        # print b[0].get_text()
        if len(b) > 0:
            company_name = ""
    return company_name


url = "https://www.bloomberg.com/markets/symbolsearch?query={ticker}&commit=Find+Symbols"
correct_companies_list = []
incorrect_companies_list = []

count = 0

ticker_check_query = """
                SELECT * FROM {table_name} where Ticker LIKE '{ticker}'
                """

correct_insert_query = """
    INSERT INTO re_ticker_list (Ticker, CompanyName, ImageName)
    VALUES ('{ticker}', '{company_name}', '{image_name}');
    """

incorrect_insert_query = """
    INSERT INTO re_incorrect_ticker_list (Ticker, CompanyName, ImageName)
    VALUES ('{ticker}', '-', '{image_name}');
    """

db = Database()

kaka_ni_tal = 0

with open('/home/jay/Desktop/ocr_output/output_Ticker_23-05-2017.txt') as fp:
    for line in fp:
        line = line.rstrip()
        if "jay" in line:
            #print "file done" + str(count)
            count = count + 1
            image_path = line
            image = line.rsplit("/", 1)[1]
            #print "Processing file %s" % image
            image_name = image
        else:
            ticker_s = remove_spaces(line)
            ticker_c = last_replace(ticker_s)
            companies = db.query(ticker_check_query.format(table_name='ticker_list', ticker=ticker_s))
            invalid_companies = db.query(ticker_check_query.format(table_name='incorrect_ticker_list', ticker=ticker_s))
            re_companies = db.query(ticker_check_query.format(table_name='re_ticker_list', ticker=ticker_s))
            re_invalid_companies = db.query(ticker_check_query.format(table_name='re_incorrect_ticker_list', ticker=ticker_s))
            if len(companies) > 0 or len(invalid_companies) > 0 or len(re_companies) > 0 or len(re_invalid_companies) > 0:
                kaka_ni_tal = 1
                #print "%s ticker already exists" % ticker_s
            else:
                bm_url = url.format(ticker=ticker_c)
                parsed = requests.get(bm_url)
                soup = BeautifulSoup(parsed.content, 'html.parser')
                firm_name = check_ticker(soup, ticker_c)
                if firm_name:
                    firm_name = firm_name.replace(r"'", r"\'")
                    firm_name = firm_name.replace('"', r'\"')
                    print firm_name
                    print "image %s"%image_name
                    print "inserting firm name for %s"%ticker_c
                    db.insert(
                        correct_insert_query.format(ticker=ticker_s, company_name=firm_name, image_name=image_path))
                else:
                    print "didn't get firm name for %s"%ticker_c
                    db.insert(
                        incorrect_insert_query.format(ticker=ticker_s, image_name=image_path))

