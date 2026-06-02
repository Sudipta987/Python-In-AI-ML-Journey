#String properties and their different functions in Python

#Concatenation
print("Hello"+"World")

# Lenght of the String 
str1=str(input("Enter as your wish : "))

# str1[0]='@' #TypeError: 'str' object does not support item assignment
# Indexing 
print(str1[0])
print(str1)
print(len(str1))

# Slicing : Accessing an specific parts of a String
# Syntax : str[starting_idx : ending_idx]  # where endig idx is not included
str2="0123456789"

print(str2[3 : 9])
print(str2[5:]) # It automatically takes the last idx
print(str2[:9]) # It automatically takes the Begining idx
# Slicing with Negative Index
print(str2[-4:])
print(str2[-1:-4:-1])

# STRING FUNCTIONS 
print(str1.endswith(".")) # returns true if string ends with substr
print (str1.capitalize()) # capitalizes 1st char
print(str1.replace("World","Universe")) # replaces all occurances of old with new
print(str1.find("Best")) # returns 1st idx of 1st occurrence
print(str1.count("the")) # counts the occurrence of substr in string

