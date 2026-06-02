#Expression Execution
#String & Numeric values can operate together with *
A,B=2,3
Txt="@"
print(2*Txt*3) # op = @@@@@@

#String & String can operate with + 
C,D="2",3
print((C+Txt)*D) # op = 2@2@2@

#Numeric values can operate with all arithmetic operators
print(A+B*D)
#Arithmetic Expression wiht Integer and Float will Result in Float
print(3*3.14)

#Result of division operator with two integers will be float

#Integer division wiht float and int will give int displayed as float
X,Y=1.5,3
Z=X//Y
print(Z,X/Y)

#Remainder is negative when dennominator is negative

""" This is an 
Multi-line Comment in Python"""