# Create a set
# Set items are unordered, unchangeable, and do not allow duplicate values.
this_set = {"Imran", "Najma", "Tamim"}
print(this_set)

print("The length  of the set is = ", len(this_set))

set1 = {"abc", 34, True, 40, "male"}
print(set1)

# Loop through the set, and print the values:
for x in set1:
    print(x)

# Check if Banana is present on the set
thisset = {"apple", "banana", "cherry"}

print("Yes ! banana is present on the thisset = ", "banana" in thisset)

# Add an item to a set, using the add() method:

thisset.add("orange")
print("After add a new value on the set = ", thisset)

# Add a set to another set
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print("Two set has merge with update method = ", thisset)

# Remove a set item

thisset.remove("cherry")
print("After remove the cherry the set is now =", thisset)
thisset.pop()
print("After remove random item using pop =", thisset)

# Join 2 set

set3 = set1.union(thisset)
print("\nAfter join 2 sets = ", set3)

# Delete all the set

thisset.clear()
print("after delete all the set ", thisset)

# Set Methods
# Python has a set of built-in methods that you can use on sets.
#
#       Method	                    Description
#       add()	                    Adds an element to the set
#       clear()	                    Removes all the elements from the set
#       copy()	                    Returns a copy of the set
#       difference()	            Returns a set containing the difference between two or more sets
#       difference_update()	        Removes the items in this set that are also included in another, specified set
#       discard()	                Remove the specified item
#       intersection()	            Returns a set, that is the intersection of two other sets
#       intersection_update()	    Removes the items in this set that are not present in other, specified set(s)
#       isdisjoint()	            Returns whether two sets have a intersection or not
#       issubset()	                Returns whether another set contains this set or not
#       issuperset()	            Returns whether this set contains another set or not
#       pop()	                    Removes an element from the set
#       remove()	                Removes the specified element
#       symmetric_difference()	    Returns a set with the symmetric differences of two sets
#       symmetric_difference_update() inserts the symmetric differences from this set and another
#       union()	                    Return a set containing the union of sets
#       update()	                Update the set with the union of this set and others
