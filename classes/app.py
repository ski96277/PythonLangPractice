from person import Person

personObj = Person(name="Imran",age=28)

print("Person name is = ", personObj.name)
print("Person age is = ", personObj.age)
print("Person age is = ", personObj.__str__())
print("Person get name function = ", personObj.get_name())

# modification the age
personObj.age = 40

print("Get modified age by getAge function = ", personObj.age)


