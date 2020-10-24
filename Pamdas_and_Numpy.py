# IBM Data Science Week 4
# Author: Christopher Jones
# Date: October 22, 2020
# Video 3: Loading data with Pandas / Working with and saving data
# Part 1
import pandas as pd
import numpy as np
"""
# Loading data would look something like
csv_path = file1.csv  #stores path of csv
df = pandas.read_csv(csv_path) #result is stored in variable df which represents dataframe
df.head() #examines first 5 rows of dataframe

# Practice dataset
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj', 'Chris', 'Jones', 'Windsor', 'Mike', 'Jet', 'Smith'],
        'Age':[27, 24, 22, 32, 22, 23, 19, 40, 53, 37],
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj', 'Branch', 'Brook', 'Court', 'Knotty', 'Philly', "Bmore"],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd', 'MBA', 'CPA', 'BA', 'BS', 'MCA', 'Phd']}

df = pd.DataFrame(data)
print(df.head())
# Creates a new dataframe of the specified columns
# print(df[['Name', 'Qualification']])
print("##############################################")

# loc is primarily label based; 
# when two arguments are used, you use column headers and row indexes to select the data you want. 
# loc can also take an integer as a row or column number.
# loc will return a KeyError if the requested items are not found. 
print(df.loc[0,'Name'])
print(df.loc[1,'Age'])
print(df.loc[2,'Address'])
print(df.loc[3,'Qualification'])
print("##############################################")

# iloc is integer-based. 
# You use column numbers and row numbers to get rows or columns at particular positions in the data frame.
# iloc will return an IndexError if the requested indexer is out-of-bounds.

print(df.iloc[0,0]) # row 1, col 1
print(df.iloc[1,0]) # row 2, col 1
print(df.iloc[0,1]) # row 1, col 2
print(df.iloc[1,1]) # row 2, col 2
print(df.iloc[2,0]) # row 3, col 0
print(df.iloc[0,2]) # row 0, col 3
print(df.iloc[2,1]) # row 3, col 2
print(df.iloc[1,2]) # row 2, col 3
print(df.iloc[2,2]) # row 3, col 3
print(df.iloc[3,3]) # row 4, col 4
print("##############################################")

# By default, ix looks for a label. 
# If ix doesn't find a label, it will use an integer. 
# This means you can select data by using either 
# column numbers and row numbers or column headers and row names using ix.


# You can also slice data frames and assign the values to a new data frame using the column names.

slice1 = df.iloc[0:2, 0:2]
print(slice1)
print("##############################################")

################################################################
# Part 2
# Grabs you all the unique value from a given column/category
print(df['Qualification'].unique())
#ageQual1 = df['Age'] >= 30  : Not sure what this does or why it outputs what it does. Check back later
New_df = df[df['Age'] >= 30]
#print(ageQual1) #Check back later
print(New_df)
#New_df.to_csv("Age_requirement.csv")
"""
# Practice from IBM Notebooks
csv_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.csv'
df = pd.read_csv(csv_path)
print(df.head())
print("##############################################")

xlsx_path = 'https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/PY0101EN/Chapter%204/Datasets/TopSellingAlbums.xlsx'
df2 = pd.read_excel(xlsx_path)
print(df2.head())
print("##############################################")

# Access to the column Length
x = df[['Length']]
print(x)
print("##############################################")

# Get the column as a series
y = df['Length']
print(y)
print("##############################################")

# Get the column as a dataframe
z = type(df[['Artist']])
print(z)
print("##############################################")

# Access to multiple columns
a = df[['Artist','Length','Genre']]
print(a)
print("##############################################")

# Use a variable q to store the column Rating as a dataframe
b = df[['Rating']]
print(b)
print("##############################################")

# Assign the variable q to the dataframe that is made up of the column Released and Artist:

c = df[['Released','Artist']]
print(c)
print("##############################################")

# Access the 2nd row and the 3rd column of df:
d = df.iloc[1,2]
print(d)
print("##############################################")






