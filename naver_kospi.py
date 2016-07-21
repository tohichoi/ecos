#!/usr/bin/env python
# encoding: utf-8

import bs4
import sys
import urllib2
import io
import pandas as pd
import pickle
import time


'''
N
종목명
현재가
전일비
등락률
액면가
시가총액
상장주식수
외국인비율
거래량
PER
ROE
토론실
'''

hdr=('N', '종목명', '현재가', '전일비', '등락률', '액면가', '시가총액', '상장주식수', '외국인비율', '거래량', 'PER', 'ROE', '토론실')

def read_one_page(url):

	print url

	fd=urllib2.urlopen(url)
	html=io.BytesIO(fd.read())

	soup = bs4.BeautifulSoup(html)

	data = []
	hdrs = None
	table = soup.find('table', attrs={'class':'type_2'})
	#table = soup.find_all('table', 'type_2')
	if not table:
		print 'Table type_2 not found'
		sys.exit(1)

	table_body = table.find('tbody')

	rows = table_body.find_all('tr')
	for row in rows:
		cols = row.find_all('td')
		cols = [ele.text.strip() for ele in cols]
		if len(cols) > 1:
			#data.append([ele for ele in cols if ele]) # Get rid of empty values
			data.append(cols)

	#print hdrs
	# for r in data:
	# 	if len(r) > 0:
	# 		print r

	return data


def generate_filename():
	
	tm=time.localtime()

	fn='naver_kospi_volume_%02d%02d%02d_%02d%02d%02d.pickle' % (tm.tm_year-2000, tm.tm_mon, tm.tm_mday, tm.tm_hour, tm.tm_min, tm.tm_sec)

	return fn

s=1
e=25

url='http://finance.naver.com/sise/sise_market_sum.nhn?&page=%d'

dflist=[]

for i in range(s, e+1):
	data=read_one_page(url % i)
	df2=pd.DataFrame(data, columns=hdr)
	dflist.append(df2)

df=pd.concat(dflist)

fn=generate_filename()

fd=open(fn, 'w+')
pickle.dump(df, fd)
fd.close()

