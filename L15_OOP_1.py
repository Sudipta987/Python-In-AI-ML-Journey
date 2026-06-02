#OOP in Python: To map real world scenarios, we started using objects in code.
# This is called object oriented programming.
#Class & Object in Python: Class is a blueprint for creating objects.
# Creating Class
class Car : 
    color="blue"
    brand="mercedes"


#Creating Object
c1=Car()
print(c1.color)
print(c1.brand)
# __init__ Function : Constructor 
# All Classes have a function called __init__(), which is always executed when the class is being initiated.
class Student : 
    clg_name="ABC College"  # This is an Class Attribute since all instance have the same College
    def __init__(self,name) :  #Student.__init__() takes 0 positional arguments but 1 was given
        print("Creating new studient in db")
        print(self)
        self.name=name  # This is an Instance/Obj Attribute since all instance will have different name value
    def welcome(self) :
        print("Welcome Student : ",self.name)

s1=Student("Sudipta")
s1.welcome()
s1.name="Sudipta kar"
print(s1.name)
print(s1.clg_name)
print(Student.clg_name)
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class. (similer to java,s this keyword)
# NOTE : obj attr > class attr 


# Static Methods : Methods that don't use the self parameter (work at class level)
class Students : 
    @staticmethod # decorator
    def hello():
        print("Hello Students !")

s2=Students()
Students.hello()
s2.hello()

# Abstraction : Hiding the implementation details of a class and only showing the essential features to the user.

# Encapsulation : Wrapping data and functions into a single unit(Object).