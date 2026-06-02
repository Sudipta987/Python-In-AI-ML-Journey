# File I/O in Python : Python can be used to perform operations on a file.(read & write data)
# Types of all files: 
# 1.Text Files: .txt, .docx, .log etc.
# 2.Binary Files: .mp4,.mov,.png, .jpeg etc.
# Character | Meaning
# 'r' : open for reading (default)
# 'w' : open for writing, truncating the file first
# 'x' : create a new file and open it for writing
# 'a' : open for writing, appending to the end of the file if it exists
# 'b' : binary mode
# 't' : text mode (default)
# '+' : open a disk file for updating (reading and writing)
# Refer this for exploring different file modes : https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-the-built-in-open-function
# OPEN , READ & CLOSE FILE: We have to open a file before reading or writing.
# Syntax: f=open("file_name","mode") | "file_name"=e.g, sample.txt,demo.docx and "mode"=e.g,r:read w:write mode
# data=f.read() f.close()

f=open("demo.txt","r")
data=f.read() # we can alos use parameter e.g, f.read(5) reads only first 5 characters
data1=f.readline() # reads one line at a time but here it only retrun an "" new line cause : earlier f.read() function reads the eintre file now it makes the current pointer as EOF .
print(data)
print(data1)
print(type(data))
f.close()

# Writing to a file : 
# f=open("demo.txt","w")   # It overwrites the entire file & if file does't exists it automatically creates the file with "demo.txt" name
f=open("demo.txt","a") # It only adds at the end of the file & if file does't exists it automatically creates the file with "demo.txt" name

# f.write("I have to enter the core ML in python from tomorrow")
f.write("\nThen I have to learn AI concepts e.g, LLM,RAG etc.")
f.close()

f=open("demo.txt","r+") # read+ overwrite (Pointer at start)
f.write("abc")
print(f.read())
f.close()

# with Syntax
with open("demo.txt","r") as f :  # here with syntax automatically close the file
    data=f.read()
    print(data)

# Deleting a File: using the os module
# Module (like a code library) is a file  written by another programmer that generally has a functions we can use.
import os
os.remove("sample.txt")