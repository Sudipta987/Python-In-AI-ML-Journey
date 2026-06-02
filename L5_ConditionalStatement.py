# Conditional Statements in Python

"""if(condition):
    Statement1
elif(condition):
    Statement2
else:
    StatementN"""

light=input("Enter the Light Color: ");

if(light=="red"):
    print("Stop")
elif(light=="green"):
        print("Go")
elif(light=="orange"):
        print("Ready to Stop")
else:
       print("light is broken")

marks=int(input("Enter your marks"))

if(marks>=90) :
       print("A")
elif(marks>=80):
       print("B")
elif(marks>=30 and marks<=40):
      print("Passed")
elif(marks>=40 and marks<=80):
       print("Average")
else:
       print("Better Luck next time")

# Ternary Operator in Python

food=input("Enter your Favorit Food: ")
eat="Yes" if food=="cake" else "no"
print(eat)

print("sweet") if food=="cake" or food=="jalebi" else print("not sweet")

#Ternary Operator / Clever IF
age=int(input("Enter your age: "))
vote=("yes","no") [age<18]
print(vote)
sal=float(input("Enter your salary: "))

tax=sal*(0.1,0.2) [sal>=50000]
print(tax)
# Alternative of SWITCH  in Python is MATCH CASE
light = "green"

match light:
    case "red":
        print("Stop")
    case "green":
        print("Go")
    case "orange":
        print("Ready to Stop")
    case _:
        print("Light is broken")
