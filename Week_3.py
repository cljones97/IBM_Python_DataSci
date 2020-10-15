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

