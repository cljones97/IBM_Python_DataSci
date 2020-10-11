# IBM Data Science Week 2
# Author: Christopher Jones
# Date: October 5, 2020
# Video 1: Tuples & List

# Tuples are an ordered sequence 
# Tuples are written as comma separated elements within parenthesis 
# Tuple is a type of variable 
# Tuples can contain strings, ints and floats but are still defined as a type tuple

# A Tuple example: 
Ratings = (10, 9, 5, 7, 6, 9, 4, 2, 2, 8)

Tuple1 = ("disco", 1, 5.5)

# Indexing of tuple examples
print(Tuple1[0])
print(Tuple1[1])
print(Tuple1[2])

# Negative indexing
print(Tuple1[-1])
print(Tuple1[-2])
print(Tuple1[-3])

# Concatanate tuples
Tuple2 = Tuple1 + ("Hard rock", 20)
print(Tuple2)
# Slicing Tuples (Get elements 0 TO 3....not through 3)
print(Tuple2[0:3])

# Tuples are immutable which means they can't be changed
# In order to sort we must create a separate variable
RatingsSorted = sorted(Ratings)
print(RatingsSorted)

# A tuple can also be nested

NestedTuple = (1, 2, ("pop", "rock"), (3, 4), ("disco", "ball", (1, 2)))
print(NestedTuple[4])
print("##############################################")
###########################################################################
# List
# List are also ordered sequence
# List are represented with square brackets and are not immutable 

List1 = ["MJ", 10, 1.5]
print(List1)
# List splicing
print(List1[1:3])
# Concatanate
List2 = List1 + ["pop", "out", 20]
print(List2)
# OR instead of making a new list
List1.extend(["yessir", "chris jones"])
print(List1)
# Append adds the necessary elements to the list but in one index
List1.append(["Who", "is", "this"])
print(List1)

# Delete an index
del(List1[0])
print(List1)

# Convert a string into a list
String1 = "Chris Jones"
print(String1.split())
String2 = "A, B, C, D"
print(String2.split(","))

