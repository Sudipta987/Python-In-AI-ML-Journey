#OOP in Python: To map real world scenarios, we started using objects in code.
# And here, we will see after the Abstraction and Encapsulation of opps which bears the rest of OOP

# del keyword : used to delete object properties or object itself.
class Student : 
    def __init__(self,name) :
        self.name=name

s1=Student("Sudipta")
print(s1)
del s1 
# print(s1) #NameError: name 's1' is not defined

# Private(like) attributes & methods : Private attributes &  methods are meant to be used only within the class and are not accessible from outside the class.
print("Private concept concept-->")
class Account : 
    def __init__(self,acc_no,acc_pass) :
        self.acc_no=acc_no
        # self.acc_pass=acc_pass  # This is by default public
        self.__acc_pass=acc_pass  # Now this is private
    def reset_pass(self) : 
        print(self.__acc_pass)

acc1=Account("1234","abcd")
acc1.reset_pass();
print(acc1.acc_no)
# print(acc1.__acc_pass)  # Not accessble here - 'Account' object has no attribute '__acc_pass'

class Person : 
    __name="anonymous"
    def __hello(self) : 
        print("hello person",end=" ")
    def welcome(self):
        self.__hello();
        print(self.__name)

p1=Person()
p1.welcome();

# INHERITANCE : when one class(child/derived) derives the properties & methods of another class(parent/base).
print("Inheritance Concept--->")
class Car :
    @staticmethod
    def start() :
        print("Car Started..")

    @staticmethod
    def stop():
        print("Car Stopped.")

class ToyotaCar(Car) :  # Single Inheritance
    def __init__(self,brand):
        self.brand=brand

class Fortuner(ToyotaCar) :  # Muliti-level Inheritance
    def __init__(self,type) :
        self.type=type
        super().__init__("Fortuner")  # Super Method

car1=Fortuner("Disel")
car1.start();
print(car1.brand)

class A : 
    varA="Welcome to Class A"

class B : 
    varB="Welcome to Class B"

class C(A,B) :   # Multiple Inheritance
    varC="Welcome to Class C"

c1=C() 
print(c1.varC)
print(c1.varB)
print(c1.varA)

# Class Method : A class method is bound to the class & receives the class as an implicit first argument.
# NOTE : static method can't access or modify class state & generally for utility.
class Persons : 
    name="anonymous"
    # def change_name(self,name) :
    #     # Persons.name=name | self.__class__.name=name
    #     self.name=name
    @classmethod
    def change_name(cls,name):
        cls.name=name

p1=Persons()
p1.change_name("Rahul Kumar")
print(p1.name)
print(Persons.name)

# Polymorphism : Operator Overloading - when the same operator is allowed to have different meaning according to the context.
class Complex:
    def __init__(self,real,img) :
        self.real=real
        self.img=img
    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    def __add__(self,num2) :   # Now it's an Dunder function
        newReal=self.real+num2.real
        newImg=self.img+num2.img
        return Complex(newReal,newImg)
    def __sub__(self,num2) :   # Now it's an Dunder function
        newReal=self.real-num2.real
        newImg=self.img-num2.img
        return Complex(newReal,newImg)

num1=Complex(1,3)
num1.showNumber()

num2=Complex(4,6)
num2.showNumber()

# num3=num1.add(num2)
# num3=num1+num2
num3=num1-num2
num3.showNumber()