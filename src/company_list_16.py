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
    INSERT INTO new_ticker_list_2016 (Ticker, CompanyName, ImageName)
    VALUES ('{ticker}', '{company_name}', '{image_name}');
    """

incorrect_insert_query = """
    INSERT INTO new_incorrect_ticker_list_2016 (Ticker, CompanyName, ImageName)
    VALUES ('{ticker}', '-', '{image_name}');
    """

db = Database()

check_now = True

with open("/home/jay/Desktop/ocr_output/customers1_correct_available_tickers_17_output_customers1_correct_available_tickers.txt") as fp:
    for line in fp:
        line = line.rstrip()
        if "jay" in line:
            print "file done" + str(count)
            count = count + 1
            image_path = line
            image = line.rsplit("/", 1)[1]
            print "Processing file %s" % image
            image_name = image
            check_now = True
        else:
            if check_now:
                check_now = False
                ticker_s = remove_spaces(line)
                ticker_c = last_replace(ticker_s)
                companies = db.query(ticker_check_query.format(table_name='new_ticker_list_2016', ticker=ticker_s.replace("'", "\\'")))
                invalid_companies = db.query(ticker_check_query.format(table_name='new_incorrect_ticker_list_2016', ticker=ticker_s.replace("'", "\\'")))
                if len(companies) > 0 or len(invalid_companies) > 0:
                    print "%s ticker already exists" % ticker_s
                else:
                    bm_url = url.format(ticker=ticker_c)
                    parsed = requests.get(bm_url)
                    soup = BeautifulSoup(parsed.content, 'html.parser')
                    firm_name = check_ticker(soup, ticker_c)
                    if firm_name:
                        print "inserting firm name for %s"%ticker_c
                        db.insert(
                            correct_insert_query.format(ticker=ticker_s.replace("'", "\\'"), company_name=firm_name.replace("'", "\\'"), image_name=image_path))
                    else:
                        print "didn't get firm name for %s"%ticker_c
                        db.insert(
                            incorrect_insert_query.format(ticker=ticker_s.replace("'", "\\'"), image_name=image_path))
