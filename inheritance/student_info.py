class StudentInfo:
    def __init__(self, fName, lName):
        self.fName = fName
        self.lName = lName

    def get_fullname(self):
        return f"{self.fName} {self.lName}"
