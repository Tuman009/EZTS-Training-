class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        self.grades.append(grade)

    def average_grade(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def get_name(self):
        return self.name

    def get_grades(self):
        return self.grades


# Example usage:
students = []

# Creating instances of Student and adding grades
student1 = Student("Alice")
student1.add_grade(85)
student1.add_grade(90)
students.append(student1)

student2 = Student("Bob")
student2.add_grade(75)
student2.add_grade(80)
students.append(student2)

# Calculating and printing average grades
for student in students:
    avg_grade = student.average_grade()
    print(f"{student.get_name()}: Grades {student.get_grades()}, Average Grade: {avg_grade}")
