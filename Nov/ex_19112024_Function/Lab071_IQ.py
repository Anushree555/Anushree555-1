def sum_three(a=1,b=1,c=1):
    return a+b+c

result1=sum_three()
print(result1)

result2=sum_three(a=1, b=2)
print(result2)

result2=sum_three(a=1, b=2, c=3)
print(result2)

result2=sum_three(c=10, b=2)
print(result2)