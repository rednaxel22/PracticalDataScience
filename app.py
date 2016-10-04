# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:54:00 2016

@author: usuario
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def dataset(path, sheet_name, filter_field=None, filter_value=None):
    data = pd.read_excel(path,sheetname=sheet_name, skiprows=1, header=0)
    data = data.iloc[:,0:3]
    data = data[data.loc[:,'Year'] >= 1917]
    return data[data.loc[:,filter_field] == filter_value] 
    
def main(path, sheet_name):
    data = dataset(path, sheet_name, 'Country', 'United States')
    
    data.plot(x='Year', y=data.iloc[:,2].name, kind='bar',title='U.S. Average Income 1917-2008', legend=False)    
    ax = plt.subplot()
    ind = np.arange(len(data))
    ax.bar(ind,data.ix[:,2])
    ax.set_ylabel('Income in USD Thousands')
    start, end = ax.get_xlim()
    ax.set_xticks(np.arange(start, end, 4))
    ax.set_xticklabels(data.loc[:,'Year'][::4],rotation=45)
    
    
if __name__ == "__main__":
    main('report.xlsx', 'Series-layout A')