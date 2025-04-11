""" Build a two class call SchoolOne and SchoolTwo that display there list of students average grades and GPA. """

class Student:
    # This is the class representing a student with grades.
    
    def __init__(self, name, grades):

        self.name = name
        self.grades = grades

    def average_grade(self):

        return sum(self.grades) / len(self.grades) if self.grades else 0.0

    def gpa(self):

        avg = self.average_grade()
        if avg >= 90:
            return 4.0
        elif avg >= 80:
            return 3.0
        elif avg >= 70:
            return 2.0
        elif avg >= 60:
            return 1.0
        else:
            return 0.0


class SchoolOne:
    # This is the class representing School One with a list of students.
    
    def __init__(self):

        self.students = []

    def add_student(self, student):

        self.students.append(student)

    def display_students_info(self):

        print("School One Students:")
        for student in self.students:
            print(f"Name: {student.name}, Average Grade: {student.average_grade():.2f}, GPA: {student.gpa():.2f}")


class SchoolTwo:
    
    def __init__(self):

        self.students = []

    def add_student(self, student):

        self.students.append(student)

    def display_students_info(self):

        print("School Two Students:")
        for student in self.students:
            print(f"Name: {student.name}, Average Grade: {student.average_grade():.2f}, GPA: {student.gpa():.2f}")


# OUTPUT HERE. WITH RESPECTIVE INSTANCES, STUDENT AND SCHOOL DETAILS, AND PRINTING THE OUTPUTS AFTERWARDS.
if __name__ == "__main__":

    student1 = Student("John", [85, 90, 78])
    student2 = Student("Jane", [70, 75, 80])
    student3 = Student("Jonas", [92, 88, 95])

    school_one = SchoolOne()
    school_two = SchoolTwo()
    
    school_one.add_student(student1)
    school_one.add_student(student2)

    school_two.add_student(student3)
    
    school_one.display_students_info()
    school_two.display_students_info()