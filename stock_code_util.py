#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import pickle


def make_stock_codes():

	df=pd.read_excel('data/1. 주식 종목 리스트-v2.xlsx', thousands=',')

	df.dropna(inplace=True)

	kn='code'

	df[kn]=df[kn].apply(lambda x : '%06d' % x)

	df_new=df[[kn, 'name', 'googlecode', 'type']]
	#df_new.dropna(inplace=True)

	fd=open('stock_codes.pickle', 'w')
	pickle.dump(df_new, fd)
	fd.close()


def load_stock_codes():

	fd=open('stock_codes.pickle', 'w')
	df=pickle.load(fd)
	fd.close()

	return df


if __name__ == '__main__':

	make_stock_codes()

