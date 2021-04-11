# -*- coding: utf-8 -*-
"""
Created on Sat Apr 10 14:24:39 2021

@author: kagbaje

Exploratory data analysis of education statistics - world bank data sets 
"""

#importing libraries 
import pandas as pd
import numpy as np
import matplotlib as plt 
import seaborn as sns 




ComplteXLSX = pd.ExcelFile(r'C:\Users\931974\Documents\JupiterTest\EdStatsEXCEL.xlsx')
EDdata = pd.read_excel(ComplteXLSX, 'Data')     #main data set
EDcountry = pd.read_excel(ComplteXLSX, 'Country')  #reference data
EDseries = pd.read_excel(ComplteXLSX, 'Series')    #reference data
EDcountrySeries = pd.read_excel(ComplteXLSX, 'Country-Series') #reference data
EDcountrySeries = pd.read_excel(ComplteXLSX, 'FootNote')   #reference data
 
                               
#Majority of code was used to perform gently interrogation of the data and attempts to manipulate. With more time the intention would have been 
#to do more of the anlysis in here. Also combine the datasets with the aim of examinine the performce of a regression model that could explain the
#growth in GDP using statistic from the educational indicators.
                               
EDdata.head()

EDdata['Indicator Code'].nunique()

len(EDdata.columns)

EDdata['Indicator Code'].describe()


columnCounts = EDdata.apply(lambda x: sum(x.notnull()),axis=0)

columnCounts.describe()
#.plot(kind='bar', sort_columns = True)


EDdata.pivot_table(index='Country Name', columns='Indicator Name', values='2010',aggfunc=np.count_nonzero)


EDdataCountryYears =  EDdata.drop(['Country Code','Indicator Code','Indicator Name'], axis=1)
EDdataYears =  EDdata.drop(['Country Code','Indicator Code','Indicator Name','Country Name'], axis=1)


EDdataYears2 = EDdataYears.apply(lambda x: sum(x.notnull()),axis=1, result_type='broadcast')

EDdataYears2.mean()
EDdataYears2.describe()


EDdataYearstop10 =  EDdataYears2.sort_values('count',ascending = False).head(10)

print(EDdataYears)


groupByCountryYear = EDdataCountryYears.groupby(['Country Name']).count().reset_index()

print(groupByCountryYear)


pivot = groupByCountryYear.pivot_table(index='Country Name', columns='Indicator Name', values = '2010', aggfunc=np.count_nonzero)

pivotColumns = groupByCountryYear.columns

pivotColumns = EDdataYears.columns.difference(['Country Name','Indicator Name'])


unpivot = pd.melt(groupByCountryYear,id_vars=['Country Name'], var_name='Year', value_name='Indicators')


unpivotyear = unpivot.astype({'Year': 'int32'})
unpivotyear[unpivotyear.Year<2020]











