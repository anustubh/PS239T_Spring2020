# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 09:32:02 2020

@author: anustubh agnihotri

This script aims to introduce students to the pandas and matplotlib libraries

The students will read it a csv and then manipualte the dataframe 

They will use matplotlib to visualize the data 

The scripts borrows from multiple authors

https://github.com/dlab-berkeley/introduction-to-pandas/blob/master/introduction-to-pandas.ipynb

https://www.csdojo.io/data

"""

#read pandas df from url
import pandas as pd

countries=pd.read_csv('countries.csv')

#Inspect Data
countries.describe()
countries.head()
countries.tail()

countries[:3]

#What are the colums
countries.columns

#Subset Data 
us = countries[countries.country == 'United States']

us['population'].plot()

#Change Index
us.set_index('year',inplace=True)

#Change Col Name
us.rename(columns={'population':'pop'}, inplace= True)

us.columns

#Table 
countries['year'].value_counts()

#Aggregate 
countries.groupby('country')['population'].aggregate(max)


#Visualize

from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [1, 4, 9]
z = [10, 5, 0]
plt.plot(x, y)
plt.plot(x, z)
plt.title("test plot")
plt.xlabel("x")
plt.ylabel("y and z")
plt.legend(["this is y", "this is z"])
plt.show()

#get another country 
china = countries[countries.country == 'China']
us = countries[countries.country == 'United States']

plt.plot(us.year, us.population / 10**6)
plt.plot(china.year, china.population / 10**6)
plt.legend(['United States', 'China'])
plt.xlabel('year')
plt.ylabel('population')
plt.show()