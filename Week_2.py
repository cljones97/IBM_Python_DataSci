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
print("\n")
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
print("##############################################")
print("\n")
###########################################################################
# Video 2: Dictionaries
# If you recall, a list is integer indexes. These are like addresses.
# A list also has elements. 
# A dictionary has keys and values. The key is analogous to the index.
# They are like addresses, but they don't have to be integers. They are usually characters.
# The values are similar to the element in a list and contain information. 
# In a list each index has an element that matches to it. 
# In a dictionary those index and elements are now called Keys & Values. The key is now like an address
# To create a dictionary, we use curly brackets. The keys are the first elements.
# They must be immutable and unique. Each key is followed by a value separated by a colon.
# The values can be immutable, mutable, and duplicates. Each key and value pair is separated by a comma. 

First_Dict = { "Thriller": 1982, "Back in Black": 1980, "The Dark Side of the Moon": 1973, "The Bodyguard": 1992 }

# Print the whole dictionary
print(First_Dict)

# Get value of specific key
# Both Val1 and Val2 are doing the same thing, getting the value of a specific key
Val1 = First_Dict["The Dark Side of the Moon"]
print(Val1)
Val2 = First_Dict.get("The Dark Side of the Moon")
print(Val2)

# Changing Values
First_Dict["Thriller"] = 1984
print(First_Dict)

# Looping through Dictionary keys and Values
# Loop through all the keys in the dictionary
print("\n")
print("##### Looping Execution Start:")
for x in First_Dict:
    print(x)
# Loop through all the values in the dictionary
for x in First_Dict:
    print(First_Dict[x])
# Does the same thing as the for loop above
for x in First_Dict.values():
    print(x)
# Print out the Keys and Values of the dictionary by using the items() method
for x, y in First_Dict.items():
    print(x, y)
# Check to see if specific key is in the dictionary
if "Back in Black" in First_Dict:
  print("Yes, 'Back in Black' is one of the keys in the First_Dict dictionary") 

print("##### Looping Execution End:")
print("\n")

# Check Dictionary length
print(len(First_Dict))

# Adding and Removing Items in the Dictionary
First_Dict["Rumours"] = "1977"
print(First_Dict)

del First_Dict["Rumours"]
print(First_Dict)

# Check to see if key is in Dictionary
print("Thriller" in First_Dict)

#Print out only the Keys and only the Values in python
print(First_Dict.keys())
print(First_Dict.values())
print("##############################################")
print("\n")
###########################################################################
# Video 3: Sets

