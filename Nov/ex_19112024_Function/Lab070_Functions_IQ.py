#create pgm of 3 numbers from user input ,
# if user dont give values use default value  100,200,300

#def sum_of_three_numbers_default(num1=100,num2=200,num3=300):
   # return num1+num2+num3
##print(result)

#num1=int(input("Enter the number"))
#num2=int(input("Enter the number"))
#num3=int(input("Enter the number"))

#def sum_of_three_numbers_default(num1=100,num2=200,num3=300):
   # return num1+num2+num3
#result = sum_of_three_numbers_default()
#print(result)


num1=int(input("Enter the number"))
num2=int(input("Enter the number"))
num3=int(input("Enter the number"))

def sum_of_three_numbers_default(n1=100,n2=200,n3=300):
    return n1+n2+n3
result1=sum_of_three_numbers_default(num1,num2,num3)
print(result1)

result2 = sum_of_three_numbers_default()
print(result2)