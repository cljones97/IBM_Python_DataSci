# IBM Data Science Week 3
# Author: Christopher Jones
# Date: October 14, 2020
# Video 1: Conditions & Branching
import time


# Comparison Operators
# Checking equalities/inequalities
a = 6
b = 7
print(a == 6) # Output should return True
print(a >= 5) # Output should return True
# != is similar to <>
print(a != 5) # Output should return True
print(a != b) # Output should return True

Name1 = "Chris Jones"
Name2 = "chris jones"
# The equality operator is case sensitive
print(Name1 == Name2) # Output should return False

print("##############################################")
print("\n")
################################################################
# Branching

print("How old are you?")
time.sleep(1.5)

# Typecast the user input value to an integer so it can be accepted in the conditional branch
Age = (int(input("Input Age: ")))
if Age >= 18:
    print("You are allowed to buy Tobacco Products")
else:
    print("Go ask your prarents for some")
time.sleep(1)
print("Now have a good day")
################################################################

print("Pick a number between 0 and 10")
time.sleep(1.5)

# Typecast the user input value to an integer so it can be accepted in the conditional branch
Guess = (int(input("Input Guess: ")))
if Guess > 5:
    print("You picked a pretty good guess")
elif Guess == 5:
    print("You picked correct!")
else:
    print("You picked a shitty guess")
time.sleep(1.5)
print("Now get out")

print("##############################################")
print("\n")

################################################################
# Logic Operators

print(not(True))
print(not(False))

Birth_Year = 1997
if Birth_Year >= 2000 or Birth_Year <= 1990:
    print("You're a shitty baby")
else:
    print("You were born in the prime of Earth's existence")

Savings_Acc = 27000
if Savings_Acc >= 20000 and Savings_Acc <= 30000:
    print("You approximately have twenty something thousand in your account")

print("##############################################")
print("\n")

################################################################
# Video 2: Loops
# Specifically For loops and While loops
# For Loops

print(range(10,15))
# For loop example using range() and using a list to represent square colors
squares = ["red", "yellow", "purple", "green", "blue", "orange"]
for i in range(0, 6):
    squares[i] = "white"
print(squares)

# Use for loop to change the elements in list
ovals = ['red', 'yellow', 'green', 'purple', 'blue']

for i in range(0, 5):
    print("Before oval ", i, 'is',  ovals[i])
    ovals[i] = 'weight'
    print("After oval ", i, 'is',  ovals[i])

# For loop example looping through the list and iterate on both index and element value
circles = ["red", "black", "red", "yellow", "purple", "green", "blue", "orange", "red"]
for i, circle in enumerate(circles):
    print(i, circle)

# For loop example using len() to calculate number of elements in a list
# Setting that equal to N, then using N as part of the range() to iterate through the loop
dates = [1982, 1980, 1973]
N = len(dates)

for i in range(N):
    print(dates[i])     

# While Loops
# Only run when conditions are met
# Write a while loop to copy the strings 'red' of the list squares to the list new_circles. 
# Stop and exit the loop if the value on the list is not 'red':
New_circles = []
j = 0
while(circles[j] == "red"):
        New_circles.append(circles[j])
        j = j + 1
print(New_circles)

# Write a while loop to display the values of the Rating of an album playlist stored in the list PlayListRatings.
# If the score is less than 6, exit the loop. 
# The list PlayListRatings is given by: PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
PlayListRatings = [10, 9.5, 10, 8, 7.5, 5, 10, 10]
i = 1
Rating = PlayListRatings[0]
while(Rating >= 6):
    print(Rating)
    Rating = PlayListRatings[i]
    i = i + 1


# Quiz question about the following output. 
# Output should be 11, 22, 33. 
# 2*A would output the A list, twice, for each iteration through
# 2*a outputs the iteration number, twice.
A=['1','2','3']
for a in A:
  print(2*a)


print("##############################################")
print("\n")

################################################################
# Video 3: Functions

# Function that adds 1 to a
def add(a):
    b = a + 1
    # print(a, "if you add one", b)
    return(b)

print(add(1))
print(add(2))
print(add(3))

# Function to multiply two integers
def Mult(a, b):
    c = a * b
    return(c)
    # print('This is not printed')
    
result = Mult(12,2)
result2 = Mult(10.0, 3.14)
result3 = Mult(2, "Michael Jackson ")
print(result)
print(result2)
print(result3)

album_rat = [9.5, 8.0, 7.8, 9.3, 8.4, 8.7, 8.8, 6.3, 9.8]
print(sum(album_rat))
print(len(album_rat))
print(sorted(album_rat))

def PrintList(the_list):
    for element in the_list:
        print(element)

print(PrintList(album_rat))

# Squares the input parameter, then add 1
def square(a):
    
    # Local variable b
    b = 1
    c = a * a + b
    # print(a, "if you square + 1", c) 
    return(c)

print(square(4))

# Using the square function with global variables
x = 3
# Makes function call and return function a y
y = square(x)
print(y)

# Define the function for combining strings

def con(a, b):
    return(a + b)

print(con("Chris ","Jones "))

def Equation(a,b):
    c = a + b + 2 * a * b - 1
    if(c < 0):
        c = 0 
    else:
        c = 5
    return(c) 

print(Equation(3,4))

def printAll(*args): # All the arguments are 'packed' into args which can be treated like a tuple
    print("No of arguments:", len(args)) 
    for argument in args:
        print(argument)
#printAll with 3 arguments
printAll('Horsefeather','Adonis','Bone')
#printAll with 4 arguments
printAll('Sidecar','Long Island','Mudslide','Carriage')

def printDictionary(**args):
    for key in args:
        print(key + " : " + args[key])

printDictionary(Country='Canada',Province='Ontario',City='Toronto')

def addItems(list):
    list.append("Three")
    list.append("Four")

myList = ["One","Two"]
addItems(myList)
print(myList)
    
print("##############################################")
print("\n")

################################################################
# Video 4: Objects & Classes
# Python classes and objects notebook code I was unable to get running

# Create a class Circle
"""
class Circle(object):
    
    # Constructor
    def __init__(self, radius=3, color='blue'):
        self.radius = radius #Data Attributes
        self.color = color #Data Attributes
    
    # Method
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
    
    # Method
    def drawCircle(self):
        plt.gca().add_patch(plt.Circle((0, 0), radius=self.radius, fc=self.color))
        plt.axis('scaled')
        plt.show()  
"""