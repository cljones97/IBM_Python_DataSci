# IBM Data Science Week 4
# Author: Christopher Jones
# Date: October 22, 2020
# Video 3: Loading data with Pandas / Working with and saving data
# Part 1

#!/usr/bin/env python
import time 
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#%matplotlib inline  

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
print("\n")

################################################################
# Numpy 1D



def Plotvec1(u, z, v):
    
    ax = plt.axes()
    ax.arrow(0, 0, *u, head_width=0.05, color='r', head_length=0.1)
    plt.text(*(u + 0.1), 'u')
    
    ax.arrow(0, 0, *v, head_width=0.05, color='b', head_length=0.1)
    plt.text(*(v + 0.1), 'v')
    ax.arrow(0, 0, *z, head_width=0.05, head_length=0.1)
    plt.text(*(z + 0.1), 'z')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

def Plotvec2(a,b):
    ax = plt.axes()
    ax.arrow(0, 0, *a, head_width=0.05, color ='r', head_length=0.1)
    plt.text(*(a + 0.1), 'a')
    ax.arrow(0, 0, *b, head_width=0.05, color ='b', head_length=0.1)
    plt.text(*(b + 0.1), 'b')
    plt.ylim(-2, 2)
    plt.xlim(-2, 2)

# Assign a numpy list
List1 = np.array([0, 1, 2, 3, 4])
print("Element[0]:", List1[0])
print("Element[1]:", List1[1])
print("Element[2]:", List1[2])
print("Element[3]:", List1[3])
print("Element[4]:", List1[4])

# Check the type of the array
print(type(List1))
# Check the type of the values stored in numpy array
print(List1.dtype)
print("##############################################")

# Create Numpy array
List2 = np.array([20, 1, 2, 3, 4])
print(List2)
# Reassign first and last element
List2[0] = 100
List2[4] = 0
print(List2)

# Slice List2 and reassign values to new list, elements 1 to 3
List3 = List2[1:4]
print(List3)

# Get the size of numpy array
print("Size = ", List2.size)
# Get the number of dimensions of numpy array
print("Num of dimensions = ", List2.ndim)
# Get the shape/size of numpy array
print("Shape = ", List2.shape)
# Get the mean of a numpy array
print("Mean = ", List2.mean())
# Get the standard deviation of a numpy array
print("Stan Dev = ", List2.std())

New_npArr = np.array([-50, 2, 23, 113, 430])
Sec_npArr = np.array([-23, -9, 13, 79, 213])
max_npArr = New_npArr.max()
min_npArr = New_npArr.min()

Add_np = New_npArr + Sec_npArr
Mult_np = New_npArr * Sec_npArr
Mult_np2 = New_npArr * 2
# Dot product
Dot_np = np.dot(New_npArr, Sec_npArr)

print("Max Val Numpy Array = ", max_npArr)
print("Min Val Numpy Array = ", min_npArr)
print("Added Val of Numpy Arrays = ", Add_np)
print("Mulitply Numpy Arrays = ", Mult_np)
print("Mulitply Numpy Array by 2 = ", Mult_np2)
print("Dot Proudct of Numpy Arrays = ", Dot_np)


# Python Plotting 

print(np.linspace(-2, 2, num=5))
# Makeup a numpy array within [-2, 2] and 9 elements
np.linspace(-2, 2, num=9)
# Makeup a numpy array within [0, 2π] and 100 elements 
x = np.linspace(0, 2*np.pi, num=100)
# Calculate the sine of x list
y = np.sin(x)
# Plot the result
plt.plot(x, y)

# The value of pi: np.pi
# Create the numpy array in radians: x = np.array([0, np.pi/2 , np.pi])
# Calculate the sin of each elements: y = np.sin(x)

u = np.array([1, 0])
v = np.array([0, 1])
z = u + v
print(Plotvec1(u, z, v))


################################################################
# Numpy 2D

# Create a list
NewList = [[11, 12, 13], [21, 22, 23], [31, 32, 33]]
# Convert list to Numpy Array
# Every element is the same type
TwoD = np.array(NewList)
print(TwoD)
print("# of dim = ", TwoD.ndim)
print("Size = ", TwoD.size)
print("Shape = ", TwoD.shape)

# Access the element on the second row and third column
print(TwoD[1, 2])
# Access the element on the second row and third column
print(TwoD[1][2])
# Access the element on the first row and first column
print(TwoD[0][0])
# Access the element on the first row and first and second columns
print(TwoD[0][0:2])
# Access the element on the first and second rows and third column
print(TwoD[0:2, 2])


# Create a numpy array X

NumpyX = np.array([[1, 0], [0, 1]]) 
NumpyY = np.array([[2, 1], [1, 2]]) 
NumpyZ = NumpyX + NumpyY
NumpyZ_Mult2 = 2 * NumpyZ
NumpyZ_Multiply = NumpyX * NumpyY
print("NumpyZ = ", NumpyZ)
print("NumpyZ multiplied by 2 = ", NumpyZ_Mult2)
print("NumpyZ Multiplication = ", NumpyZ_Multiply)

Mat1 = np.array([[0, 1, 1], [1, 0, 1]])
Mat2 = np.array([[1, 1], [1, 1], [-1, 1]])
Mat3 = np.array([[1,1],[2,2],[3,3]])
Mat_dot = np.dot(Mat1, Mat2)
Mat_sine = np.sin(Mat_dot)
Mat_transpose = Mat3.T

print("Matrix 1: \n", Mat1)
print("Matrix 2: \n", Mat2)
print("Matrix 3: \n", Mat3)
print("Matrix dot: \n", Mat_dot)
print("Matrix sin: \n", Mat_sine)
print("Matrix transpose: \n", Mat_transpose)