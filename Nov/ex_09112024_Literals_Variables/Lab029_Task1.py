#take 3 input from user and perform sum, sub, mul and div
num1=int(input("Enter the number1"))
num2=int(input("Enter the number2"))
num3=int(input("Enter the number3"))

sum=num1+num2+num3
sub=num1-num2-num3# we can use abs if we dont want to see negative value or if client needs
mul=num1*num2*num3
div=num1/num2/num3

print("The sum is :", sum)
print("The sub is :", sub)
print("The mul is :", mul)
print("The div is :", div)