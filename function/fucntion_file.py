def my_function():
    print("Hello my print")


def my_function2(fname, lname):
    print("My full name is ", fname, lname)


# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.
#
# This way the function will receive a tuple of arguments, and can access the items accordingly:

def my_function3(*names):
    print("name number 2 is    ", names[2])


# Default Parameter Value
def my_function4(name="Imran"):
    print("My name is = ", name)


def my_function5():
    pass


# Keyword-Only Arguments
# To specify that a function can have only keyword arguments, add *, before the arguments:
def my_function_keyword_arg(*, x, y):
    print(x, y)


# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.
#
# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
#

def my_function_position_only_and_keyword(a, b, c, /, *, d, e):
    print("pramametters are ", a, b, c, d, e, )


# Recursion
# Python also accepts function recursion, which means a defined function can call itself.

def recursion_function(*, x):
    if x > 5:
        print("x is ", x)
        x -= 1
        recursion_function(x=x)
    else:
        print("Completed the recursion function and the x is x=",x)
