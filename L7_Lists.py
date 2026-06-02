# Lists in Python : A built-in data type that stores set of values
# It can store elements of different types(Integer, Float, String ,etc.)

marks=[94.4, 87.5, 95.2, 66.4, 45.1]

print(marks)
print(type(marks))
print(marks[0],marks[1])
print(len(marks))

student=["Sudipta kar",99.99,22,"Kolkata"]
print(student)
student[0]="SUDIPTA"
print(student)

# List Slicing : Similar to String Slicing
# Syntax : list_name[starting_idx : ending_idx] # ending idx is excluded

sliceMarks=marks[1 : 3]
print(sliceMarks)
print(marks[:4]) # is same as marks[0:4]
print(marks[1:]) # is same as marks[1:len(marks)]
print(marks[-3 : -1]) # is [95.2, 66.4]

# List Methods
list = [2,1,3]
list.append(4) # adds one element at hte end [2, 1, 3, 4]
list.sort()  # sorts in ascending order
list.sort(reverse=True) # sorts in descending order [4, 3, 2, 1]
list.reverse() # reverse list [1, 2, 3, 4]

list.insert(2,99) # syntax list.index(idx, el) insert element at idx
list.insert(len(list),99) # [1, 2, 99, 3, 4, 99]
list.remove(99)  # removes first occurrence of element [1, 2, 3, 4, 99]
list.pop(len(list)-1)   # list.pop(idx) removes element at idx
print(list)
