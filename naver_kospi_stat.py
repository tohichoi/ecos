#!/usr/bin/env python

import os
import pickle
import pandas as pd
import re
import datetime


data_dir='.'
data_prefix='naver_kospi_volume_'


def get_timestamp(filename):

	pat=r'_(\d\d)(\d\d)(\d\d)_(\d\d)(\d\d)(\d\d)\.pickle'

	m=re.search(pat, filename)
	if m:
		l=map(lambda x : int(x), m.groups())
		d=datetime.datetime(l[0]+2000, l[1], l[2], l[3], l[4], l[5])
		return d

	return None


df=pd.DataFrame()

datalist=[]

# get the data file
for roots, dirs, filenames in os.walk(data_dir):
	for filename in filenames:
		abspath=os.path.join(roots, filename)
		if re.search(data_prefix, filename):
			d=get_timestamp(filename)
			if d:
				datalist.append((d, abspath))

#for data in datalist:
#	print data[0], data[1]