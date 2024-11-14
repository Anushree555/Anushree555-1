#for i in range(1, 100):
   # if i % 3 == 0 and i % 5 == 0:
       # print("FizzBuzz")
   # elif i % 3 == 0:
       # print("Fizz")
   # elif i % 5 == 0:
       # print("Buzz")
  #  continue ## pass can also be use or else: print Nothing

for i in range(1, 100):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    pass

