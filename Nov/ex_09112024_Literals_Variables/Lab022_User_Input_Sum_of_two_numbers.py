#write a pgm to take user input and then sum the number
#logic building
#step1
#input ----int/float------>>DAA as k client what they want and in what form they want
#output--sum-int, sub-int, div-float

#step2
#rough logic
#+-*/

#step3
#logic

from xmlrpc.client import MultiCall

num1=int(input("Enter the num 1"))
num2=int(input("Enter the num 2"))
print(type(num1))
print(type(num2))
Sum=num1+num2
Sub=num1-num2
Mul=num1*num2
Div=num1/num2

print("Sum is ->",Sum)
print("Sub is ->",Sub)
print("Mul is ->",Mul)
print("Div is ->",Div)
