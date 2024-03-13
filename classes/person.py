class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"

    # Create custom function inside the class
    def get_name(self):
        return self.name

    # Create custom function
    def getAge(self):
        return self.age
