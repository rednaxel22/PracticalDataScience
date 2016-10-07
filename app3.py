# -*- coding: utf-8 -*-
"""
Created on Fri Oct  7 12:42:42 2016

@author: Michael Castillo
"""

import pandas as pd
import matplotlib.pyplot as plt

def dataset(path, sheet_name, filter_field=None, filter_value=None):
    data = pd.read_excel(path,sheetname=sheet_name, skiprows=1, header=0)
    data = data[data.loc[:,'Year'] >= 1917]
    return data[data.loc[:,filter_field] == filter_value] 

def plotData(path, sheet_name):    
    data = dataset('report.xlsx', 'Series-layout A', 'Country', 'United States')
    data = data.loc[:,['Year','Top 10% income share','Top 5% income share','Top 1% income share','Top 0.5% income share','Top 0.1% income share']]
    #Normalize data with mean    
    data.iloc[:,1:] = data.iloc[:,1:] / data.iloc[:,1:].mean()    
    data.plot(x='Year', title = 'Mean Normalized U.S. Percentage Income Share')
    plt.legend(loc='center left', bbox_to_anchor=(1.0, 0.5))
    ax = plt.subplot()
    ax.set_ylabel('Percentage')

if __name__ == "__main__":
    plotData('report.xlsx', 'Series-layout A')
    
