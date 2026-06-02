# Loops in Python : Loops are used ot repeat instructions.

# while loops  - while condition : some work
print("While loop concept -->")
count=1
 
while (count<=5) : 
    if(count==4) :
        break
    print("Hello",count)
    count+=1

i=0
while(i<=5): 
    if(i==3) :
        i+=1
        continue
    print(i)
    i+=1
print("End of while loop")
# For loops are used for sequential traversal. For traversing list, string, tuples etc.
print("For loop Concept-->")
list=[1,2,3,4,5]

for val in list : 
    print(val)
else:                       # This is an optional else of for loop
    print("End of for loop")

# Need of  this optional Else 
str="I am the Best."

for char in str : 
    if(char=='e') : 
        print("e found")
        break
    print(char)
else:               # Since here the loop is not completed entirely so the ELSE is also not invoked and execute .
    print("END")

# range() : Range functions returns a sequence of numbers, starting from 0 by default
#and increments by 1(by default), and stops before a specified number.
# e.g, range(5) = 0,1,2,3,4  SYNTAX  : range(start?,stop,step?)  here ? are optional
print("Range() function concept --> ")
for i in range(10) :
    print(i)
else:
    print("End of for loop")

for i in range(3,10):
    print(i)
else: 
    print("End of for loop")

for i in range(2,10,2) : 
    print(i)
else:
    print("End of the for loop")

# pass Statement : pass is a null statement that does nothing. It is used as a placeholder
#for future code.
print("Pass statement concept-->")

for i in range(10) : 
        #empty # we can't leave this block empty[IndentationError: expected an indented block after 'for' statement on line 64]
        pass  # for this reason we need pass statement in python

print("some useful work")