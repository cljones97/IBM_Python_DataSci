# IBM Data Science Week 4
# Author: Christopher Jones
# Date: October 20, 2020
# Video 1: Reading files with Open

# Opening files method 1: 
example1 = "/Users/MasterC/IBM_Python_DataSci/Example1.txt"
# file1 = open(example1, "r")

# Opening files method 2:
# automatically closes the file 
with open(example1, "r") as file1:
    # Read certain amount of characters
    # print(file1.read(4))
    FileContent = file1.read()
    print(FileContent)
print("##############################################")
print("\n")

# Read one line
with open(example1, "r") as file1:
    print("first line: " + file1.readline())
print("##############################################")
print("\n")

# Iterate through the lines
with open(example1,"r") as file1:
        i = 0
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1
print("##############################################")
print("\n")

# Read all lines and save as a list
with open(example1, "r") as file1:
    FileasList = file1.readlines()

# Print the first line
print(FileasList[0])
print(FileasList[1])
print(FileasList[2])
print("##############################################")
print("\n")

# Print the path of file
print(file1.name)

# Print the mode of the file, either 'r' or 'w'
print(file1.mode)

# Read the file and assign it to variable
# FileContent = file1.read()

# Print the file with '\n' as a new line
# print(FileContent)

# Type of file content
print(type(FileContent))

# Close file after finish
# file1.close()

# When using "with open" method, it automatically closes the file
# We check to see if a file is closed by
# Should print out true or false
print(file1.closed)

print("##############################################")
print("\n")

################################################################
# Video 2: Writing files with Open

# Write line to file

with open('/Users/MasterC/IBM_Python_DataSci/Example2.txt', 'w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")

# Read file
# And Check whether write to file
with open('/Users/MasterC/IBM_Python_DataSci/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Write a new line to text file
# By setting the mode argument to append a you can append a new line as follows:
with open('/Users/MasterC/IBM_Python_DataSci/Example2.txt', 'a') as testwritefile:
    testwritefile.write("This is line C\n")

# Verify if the new line is in the text file
with open('/Users/MasterC/IBM_Python_DataSci/Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Sample list of text
Lines = ["This is line A\n", "This is line B\n", "This is line C\n"]

# Write the strings in the list to text file

with open('Example2.txt', 'w') as writefile:
    for line in Lines:
        #print(line)
        writefile.write(line)

with open('Example2.txt', 'r') as testwritefile:
    print(testwritefile.read())

# Copy one file to another
with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)

# Verify if the copy is successfully executed
print("This is for Example3.txt")
with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())


# Writing a file and saving in .txt format
file2 = open("myfile.txt","w")
example3 = "/Users/MasterC/IBM_Python_DataSci/myfile.txt"
L2 = ["This is Delhi \n","This is Paris \n","This is London \n"]
file2.writelines(L2)
file2.close()

print("This is for the myfile.txt")
with open(example3, "r") as file2:
    # Read certain amount of characters
    # print(file1.read(4))
    FileContent2 = file2.read()
    print(FileContent2)
