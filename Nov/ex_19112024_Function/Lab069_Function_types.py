def greet():
    print("hello")
greet()


def greet_by_name(name):
    print("hello",name)
greet_by_name("Anushree")


def say_hello_default_arg(name="Anushree"):
    print("Hello",name)
say_hello_default_arg("B N")
say_hello_default_arg()


def multiple_args(name1="A",name2="B",name3="Tc"):
    print("Mul ->",name1, name2,name3)
multiple_args()
multiple_args(name1="Anu")
multiple_args(name3="Anu")
multiple_args("LUCKY")


def sum_of_two(a, b):
    return a + b


result = sum_of_two(a= 4, b=56)
print(result)
