# Tuples in Python : A built-in Data type that lets us create immutable sequence of values

tup=(2,1,3,1)
print(type(tup))
print(tup)
print(tup[0],tup[len(tup)-1])

# tup[0]=5   # TypeError: 'tuple' object does not support item assignment since it preserve Immutable property
tup1=() # Empty tuple
print(tup1)

# tup1=(1)  # This declaration type is int  <class 'int'>
tup1=(1,) # This is valid single value tuple declaration
print(tup1)
print(type(tup1))

# Slicing in Tuples
print(tup[1:3])

# Tuple Methods 
print(tup.index(1)) # returns index of first occurrence 
print(tup.count(1)) # counts total occurrences of element