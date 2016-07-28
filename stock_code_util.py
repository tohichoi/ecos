#!/usr/bin/env python
# encoding: utf-8

import pandas as pd
import pickle
import numpy as np
import mlpy


def make_stock_codes():

	stock_name_dict=dict()
	stock_code_dict=dict()

	fn='data/truefriend-주식종목-for_google.txt'
	fd=open(fn)
	for line in fd.readlines():
		l=unicode(line.strip().decode('utf-8'))
		tokens=l.split('|')
		if len(tokens) < 1:
			continue

		# invalid line
		if len(tokens) != 3:
			print 'Error in data: ' + line
			continue

		# not a regular stock
		if tokens[0][0] in 'FG':
			continue

		if tokens[0][0] in 'Q':
			tokens[0]=tokens[0][1:]

		stock_name_dict[tokens[1]]=tokens[2]+u':'+tokens[0]
		stock_code_dict[tokens[0]]=(tokens[1], tokens[2])
	fd.close()

	fd=open('stock_name_dict.pickle', 'wb+')
	pickle.dump(stock_name_dict, fd)
	fd.close()

	fd=open('stock_code_dict.pickle', 'wb+')
	pickle.dump(stock_code_dict, fd)
	fd.close()


def load_stock_codes():

	fd=open('stock_name_dict.pickle')
	stock_name_dict=pickle.load(fd)
	fd.close()

	fd=open('stock_code_dict.pickle')
	stock_code_dict=pickle.load(fd)
	fd.close()

	return (stock_name_dict, stock_code_dict)



if __name__ == '__main__':

	#make_stock_codes()

	make_stock_codes2()

