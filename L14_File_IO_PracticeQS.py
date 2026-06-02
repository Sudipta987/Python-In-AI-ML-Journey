# W.A.P to Create a new File"Practice.txt" using python.Add the following data in it.
# Hi everyone
# we are learing File I/O
# using Java.
# I like programming in Java.
# W.A.F that replace all occurrence of "Java" with "Python" in above file.
#Search if the word "learning" exists in the file or not.

f=open("Practice.txt","w")
f.write("Hi everyone\nwe are learning File I/O\nusing Java.\nI like programming in Java.")
f.close()

with open("Practice.txt","r") as f:
    data=f.read()
print(data)
new_data=data.replace("Java","Python")
with open("Practice.txt","w") as f:
    f.write(new_data)

search_key="learning"
with open("Practice.txt","r") as f:
    data=f.read()
    if(search_key in data):
        print("Found")
    else:
        print("Not found")