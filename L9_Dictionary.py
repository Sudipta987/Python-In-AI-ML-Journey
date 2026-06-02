# Dictionary in Python : Dictionaries are used to store data values in 
# key : value pairs 
# They are unordered , mutable & don't allow duplicate keys

info ={
    "name" : "Sudipta",
    "learning" : "Coding",
    "subjects" : ["java","python","c"],
    "topics" : ("dict","sets"),
    "age" : 22,
    "isAdult" : True,
    "marks" : 99.99,
    3.14: "PI"
}

print(info)
print(type(info))
print(info["name"])
print(info[3.14])
print(info["subjects"][1])
info["name"]="SUDIPTA"
info["surname"]="KAR"
print(info)

null_dict={}
print(null_dict)

# Nested Dictionary
student={
    "name" : "Sudipta",
    "subjects" : {
        "math" : 99.9,
        "ML" : 90,
        "Ai" : 95
    }
}
print(student)
print(type(student["subjects"]))

# Dictionary Methods 
print(student.keys())  # returns all the keys
print(len(student)) # returns the lenght of the dictionary
print(student.values()) # returns all values
print(student.items()) # returns all (key, val) pairs as tuples
print(student.get("name"))  # returns the key according to value
# print(student["ML"])  # gives Error
print(student.get("ML")) # gives no Error op-> None
student.update({"city" : "Kolkata"})  # inserts the specified items to the dictionary
print(student)
new_dict={ "city" : "Kolkata","age":16}
student.update(new_dict)
print(student)