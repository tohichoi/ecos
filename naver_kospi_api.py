
# coding: utf-8

# In[2]:

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pandas_datareader import data, wb
import datetime
import pickle
import os
from scipy import fftpack
import seaborn as sns
from matplotlib.font_manager import FontProperties


# In[3]:

def load_naver_kospi_data(filename):
    
    fd=open(filename)
    df1=pickle.load(fd)
    df1.index=range(len(df1))
    df1['시가총액']=df1['시가총액'].str.replace(r'[,]', '').astype('float')
    fd.close()
    
    return df1


# In[ ]:



