# Create a dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

# Print the "brand" value of the dictionary:

print("\nPrint the brand value of the dictionary: ", thisdict['brand'])

# Duplicate values will overwrite existing values:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "year": 2020
}
print("\nDuplicate item is not existing = ", thisdict)

# Length of the dictionary

print("\n Length of the dictionary ", len(thisdict))

# Using the dict() method to make a dictionary:
thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# add a new item on the dictionary

thisdict["salary"] = 5858

print("Update the dictionary add new value = ", thisdict)

# Get all the keys
print("Get all the keys dictionary ", thisdict.keys())
# Get all the values
print("Get all the keys dictionary ", thisdict.values())

# update the values
thisdict.update({"name": "Imran sk"})
print("Update the value = ", thisdict)

# Remove an item

thisdict.pop("name")
print("dictionary after pop the name ", thisdict)

# Loop Dictionaries

for x in thisdict:
    print("Loop in dictionaries =", x)

# Copy dictionaries

newDictionaries = thisdict.copy()
print("New Copy dictionaries ", thisdict)

# Nested dictionaries
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}
print("Nested dictionaries ", myfamily)

# access item from nested dictionaries
print("access item from nested dictionaries ", myfamily["child2"]["name"])

# Python has a set of built-in methods that you can use on dictionaries.
#
#           Method	                Description

#           clear()	                Removes all the elements from the dictionary
#           copy()	                Returns a copy of the dictionary
#           fromkeys()	             Returns a dictionary with the specified keys and value
#           get()	                Returns the value of the specified key
#           items()	                Returns a list containing a tuple for each key value pair
#           keys()	                Returns a list containing the dictionary's keys
#           pop()	                Removes the element with the specified key
#           popitem()	            Removes the last inserted key-value pair
#           setdefault()	        Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
#           update()	            Updates the dictionary with the specified key-value pairs
#           values()	            Returns a list of all the values in the dictionary
