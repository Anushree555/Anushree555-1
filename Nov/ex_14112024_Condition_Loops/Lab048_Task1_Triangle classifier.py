#step1--i/p--int o/p---str
#step 2--s1,s2,s3

s1 = int(input("Enter the length of side1"))
s2 = int(input("Enter the length of side2"))
s3 = int(input("Enter the length of side3"))

if s1 == s2 == s3:
    print("It is an Equilateral triangle")
elif s1 == s2 != s3:
    print("It is an Isoceles triangle")
else:
    print("It is an Scalene triangle")
