from lambda_operation import x
from lambda_operation import my_sum

print(x(10))

# Multiply argument a with argument b and return the result:
x = lambda a, b: a * b

print(x(a=40, b=10))

# Summarize argument a, b, and c and return the result:
print(my_sum(10, 10, 10))


# Use that function definition to make a function that always doubles the number you send in:

def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)

print(mydoubler(11))
