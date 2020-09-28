# IBM Data Science Week 1
# Author: Christopher Jones
# Date: September 28, 2020
# Video 1: Types

# Identifying types
print(type(1)) 
print(type(21.223)) 
print(type("Chris Jones"))
print("###################################################")
# Type Casting
# Convert the integer 2 to a float integer of 2.0
float_cast = float(2)
# Convert the float 1.1 to an integer of 1
int_cast = int(1.1)
# Convert the string "2" to an integer of 2
string_cast = int("2")
# Convert the integer 1 to a string of 1
string_cast2 = str(1)
print("###################################################")
# when you cast a boolean False to an integer you get a 0
# bool_cast = int(FALSE)
# when you cast a boolean TRUE to an integer you get a 1
# bool_cast = int(TRUE)

# Compare float_cast (float(2)) to the float integer 2.0
print(float_cast,2.0)
# Compare int_cast (int(1.1)) to the integer 1
print(int_cast, 1)
# Compare string_cast (int("2")) to the string "2"
print(string_cast, "2")
# Compare string_cast2 (str(1)) to the string "1"
print(string_cast2, "1")
print("###################################################")
# Output the types of each
print(type(float_cast))
print(type(int_cast))
print(type(string_cast))
print(type(string_cast2))
print(int(True))
print(int(False))
print(bool(int_cast))
print(bool("hello"))
print(bool(1))
print(bool(0))
print("###################################################")

##################################################################################################
# Video 2: Expressions & Variables 
# Expressions describe a type of operation the computers perform. 
# Python follows mathematical conventions when performing mathematical expressions. 

# Addition
print(50 + 40 + 30 + 20 + 10)
# Subtraction
print(50 - 60)
# Multiplication
print(5 * 5)
# Division which leads to a float integer
print(25 / 5)
print(24 / 5)
# Division which rounds to whole number (not necessisarily the nearest whole number)
print(24 // 5)
print(30 // 8)

# Python follows mathematical conventions when performing mathematical expressions. (PEMDAS)
print(2 * 50 + 60)
print(50 - 60 + 30 * 2)
print((30 + 2) * 60)
print("###################################################")
#########################
#Variables

my_variable = 1
# my_variable:1
my_variable = 10
# my_variable:10
x = 43 + 60 + 16 + 41
# x:160
y = x / 60
#x = x / 60
#Print results
print(my_variable)
print(x)
print(y)
#Print out types
print(type(my_variable))
print(type(x))
print(type(y))

#Convert min to hours practice

total_min = 43 + 42 + 57
total_hr = (total_min / 60)
print(total_hr)




