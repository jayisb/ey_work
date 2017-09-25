import csv
from pygeocoder import Geocoder
import numpy as np

ticker_file = open("/home/jay/Pictures/bloomberg/china_tickers_g.csv")
ticker_file_reader = csv.reader(ticker_file)
tickers = []
single_row = []
rows = []
address = ""

count = 0
for row in ticker_file_reader:
	address = address + row[2] + ","
	if count == 0:
		ticker = row[0]
	count = count + 1
	if count > 3:
		print ticker
		print address.rstrip(',')
		result = Geocoder.geocode("Hekeda Industrial Area,China")
		print result.coordinates
		address = ""
		count = 0
    