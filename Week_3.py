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



