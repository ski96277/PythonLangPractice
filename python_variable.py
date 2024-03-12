name = "Imran"
age = 30
salary = 30.1
is_online = False

print("Name String = " + name)
print("Age in int = ", age)
print("Salary in double = ", salary)
print("Is online in bool = ", is_online)

# Many Values to Multiple Variables
x, y, z = "orange", "Banana", "Cherry"
print("Many Values to Multiple Variables = ", x, y, z)
# One Value to Multiple Variables
a = b = c = "orange"
print("One Value to Multiple Variables = ", a, b, c)

# If you have a collection of values in a list, tuple etc.
# Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print("First index 0 = ", x)
print("Second index 1 = ", y)
print("Third index 2 = ", z)