#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import pickle


def make_stock_codes():

	same_names={u'한국전력공사':[u'한국전력'], u'현대자동차':[u'현대차'], u'삼성전자':[u'삼성전자우']}

	df=pd.read_excel('data/1. 주식 종목 리스트-v2.xlsx', thousands=',')

	#df=df.dropna()

	kn='code'

	df[kn]=df[kn].apply(lambda x : '%06d' % x)

	stock_name_dict=dict()
	stock_krxcode_dict=dict()

	for i in range(len(df)):
		key=df['name'][i]
		stock_name_dict[key]=[df['code'][i], df[u'googlecode'][i], df['type'][i]]
		#print key
		if same_names.has_key(key):
			print key
			for l in same_names[key]:
				print l
				stock_name_dict[l]=stock_name_dict[key]

		key=df['code'][i]
		stock_krxcode_dict[key]=[df['name'][i], df[u'googlecode'][i], df['type'][i]]

	fd=open('stock_name_dict.pickle', 'wb+')
	pickle.dump(stock_name_dict, fd)
	fd.close()

	fd=open('stock_krxcode_dict.pickle', 'wb+')
	pickle.dump(stock_krxcode_dict, fd)
	fd.close()


def load_stock_codes():

	fd=open('stock_name_dict.pickle')
	stock_name_dict=pickle.load(fd)
	fd.close()

	fd=open('stock_krxcode_dict.pickle')
	stock_krxcode_dict=pickle.load(fd)
	fd.close()

	return (stock_name_dict, stock_krxcode_dict)

 
if __name__ == '__main__':

	make_stock_codes()

