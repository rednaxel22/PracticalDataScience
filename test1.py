# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 09:42:18 2016

@author: Mihcael Castillo
"""

import pandas as pd

data = pd.read_excel('report.xlsx',sheetname='Series-layout A', skiprows=1, header=0)

len(data)               # Get Dataframe rows len
data.iloc[:,0:3]        # Get all rows and firts 3 columns
len(data.columns)       # Get the columns len

data.iloc[:,0].unique() # Distinct Countries
data.iloc[:,1].unique() # Distinct Years

min(data.iloc[:,1])     # Min Year
max(data.iloc[:,1])     # Max Year

dataUS = data[data.iloc[:,0] == 'United States']    # Filter by Index
dataUS = dataUS.iloc[:,0:3]                         # Select the first 3 columns
dataUS

data[data.loc[:,'Country'] == 'United States']      # Filter by ColumnName

data.columns

data.loc[:,['Year','Country','Average income per tax unit']]