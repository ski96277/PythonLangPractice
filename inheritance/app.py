# Inheritance allows us to define a class that inherits all the methods and properties from another class.
#
# Parent class is the class being inherited from, also called base class.
#
# Child class is the class that inherits from another class, also called derived class.
from inheritance.student import Student

studentObj = Student(fName="Imran",lName="sk",graduationYear=2024)

print("Passing year = ", studentObj.graduationYear)
print("Student First Name = ", studentObj.fName)
print("Student Last Name = ", studentObj.lName)
print("Student get All info = ", studentObj.get_all_info())
print("Student get full name = ", studentObj.get_fullname())