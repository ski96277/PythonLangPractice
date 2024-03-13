topless = ("imran", "Najma", "Tamim")
print("access the Tuples by index = ", topless[1])

print("\n===========  Tuple condition ===========")

if "imran" in topless:
    print("\nImran inside the topless")
else:
    print("\nSorry! imran is not there")

# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.
#
# But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.


x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)

print("Updated topless = ", x)

# Unpack Tupless
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(*red,) = fruits

print(red)