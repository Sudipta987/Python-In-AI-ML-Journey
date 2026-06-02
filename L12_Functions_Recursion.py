# Functions in Python : Block of statement that perform a specific task.
# Syntax : def func_name(param1,param2,..) : some work return val  -> Function definition
# func_name(arg1,arg2..) # function call

def cal_sum(a,b) :
    sum=a+b
    return sum

print(cal_sum(5,6))

def print_hello() :
    print("Hello")

op=print_hello();
print(op) # None : as this function's does't return any value i.e, None

# Built-in functions e.g, print,len,type(), range()
print("Sudipta",end=" ") # sep=" " 
print("kar") #end="\n"

# Default Parameters : Assigning a default value to parameter, which is used when no argument is passed.
def cal_prod(a=1,b=1) : # remember last parameter shoud be defaul first this means we can't do (b=2,a) this give you an error.
    return a*b
print(cal_prod())

# Recursion : When a function calss itself repeatedly.
# prints n to 1 backwards
print("Recursion Concept-->")
def show(n) : 
    if(n==0) : 
        return
    print(n)
    show(n-1)
   
show(5)
# Find Factorial using Recursion
def find_fact(n) :
    if(n==0 or n==1) :
        return 1
    return n*find_fact(n-1)

print("Factorial of 5 is : ",find_fact(5))