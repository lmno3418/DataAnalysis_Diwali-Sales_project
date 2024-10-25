# import python libraries
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt # visualizing data
import seaborn as sns

# import csv file
df = pd.read_csv('Diwali_Sales_Data.csv', encoding= 'unicode_escape')

#drop unrelated/blank columns
df.drop(['Status', 'unnamed1'], axis=1, inplace=True)

# drop null values
df.dropna(inplace=True)

# change data type
df['Amount'] = df['Amount'].astype('int')

#rename column
df.rename(columns= {'Age Group':'Age_Group'}, inplace=True)

# use describe() for specific columns
df[['Age', 'Orders', 'Amount']].describe()
