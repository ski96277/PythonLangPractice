from inheritance.student_info import StudentInfo


class Student(StudentInfo):
    def __init__(self, fName, lName, graduationYear):
        self.graduationYear = graduationYear
        super().__init__(fName, lName)

    def get_all_info(self):
        return f"First name= {self.fName} last name = {self.lName}, year =  {self.graduationYear}"

    def get_graduation_year(self):
        return self.graduationYear
