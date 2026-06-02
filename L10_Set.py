# Set in Python : Set is the Collection of the Unordered items.
# Each element in the set must be unique & immutable. NOTE : SETS ARE MUTABLE BUT ITS ELEMENTS ARE IMMUTABLE
# We can't sotre list and dictionary in the Set since they are mutable.

collection={1,2,3,4,"hello","world",2,"world"} # repeated elements stored only once, so it resolved to only unique and once 
print(collection)
print(type(collection))
print(len(collection))

collection1=set() # empty set; syntax
print(type(collection1))

# Set Methods 
collection.add(3.14) # adds an element
print(collection)
collection.remove(3.14) # removes the element
print(collection)
# collection.clear()  # empties the set entirely
# print(collection)
collection.pop() # removes a random value
print(collection)

set1={1,2,3,4,5}
set2={4,5,6,7,8}

set_union=set1.union(set2) # combines both set values & returns new
print(set_union)
set_inter=set1.intersection(set2)  # combines common values & returns new
print(set_inter)

values={9,"9.0"}
print(values)