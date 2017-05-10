from bs4 import BeautifulSoup
import requests
import csv


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
        #print cn
    else:
        b = soup.findAll("div", {"class": "ticker_nomatches"})
        #print b[0].get_text()
        if len(b) > 0:
            company_name = ""
    return company_name

url = "https://www.bloomberg.com/markets/symbolsearch?query={ticker}&commit=Find+Symbols"
correct_companies_list = []
incorrect_companies_list = []

count = 0
with open('/home/jay/Desktop/sample.txt') as fp:
    for line in fp:
        line = line.rstrip()
        if "jay" in line:
            print "file done" + str(count)
            count = count + 1
            image = line.rsplit("/",1)[1]
            image_name = image
        else:
            ticker_s = remove_spaces(line)
            ticker_c = last_replace(ticker_s)
            bm_url = url.format(ticker=ticker_c)
            parsed = requests.get(bm_url)
            soup = BeautifulSoup(parsed.content, 'html.parser')
            firm_name = check_ticker(soup, ticker_c)
            tmp = []
            tmp.append(ticker_s)
            if firm_name:
                tmp.append(firm_name)
                correct_companies_list.append(tmp)
            else:
                tmp.append(image_name)
                incorrect_companies_list.append(tmp)

correct_companies_set = set(tuple(x) for x in correct_companies_list)
unique_company_list = list(correct_companies_set)
unique_company_list = [list(elem) for elem in unique_company_list]

print correct_companies_list
print correct_companies_set
print unique_company_list
print incorrect_companies_list

with open("/home/jay/Desktop/correct_kor.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(unique_company_list)

with open("/home/jay/Desktop/incorrect_kor.csv", "wb") as f:
    writer = csv.writer(f)
    writer.writerows(incorrect_companies_list)