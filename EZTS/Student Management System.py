class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.enrolled_courses = {}

    def enroll_course(self, course):
        self.enrolled_courses[course.course_code] = course

    def assign_grade(self, course_code, grade):
        if course_code in self.enrolled_courses:
            self.enrolled_courses[course_code].assign_grade(self.student_id, grade)

    def calculate_gpa(self):
        total_credits = 0
        total_weighted_grade_points = 0
        for course_code, course in self.enrolled_courses.items():
            grade = course.get_grade(self.student_id)
            credits = course.credits
            if grade is not None and credits is not None:
                total_weighted_grade_points += grade * credits
                total_credits += credits
        if total_credits > 0:
            return total_weighted_grade_points / total_credits
        else:
            return 0.0

class Course:
    def __init__(self, course_code, course_name, credits):
        self.course_code = course_code
        self.course_name = course_name
        self.credits = credits
        self.grades = {}

    def assign_grade(self, student_id, grade):
        self.grades[student_id] = grade

    def get_grade(self, student_id):
        return self.grades.get(student_id, None)


# Example usage:
# Create courses
course1 = Course("CS101", "Introduction to Computer Science", 3)
course2 = Course("ENG201", "English Literature", 4)

# Create students
student1 = Student(1, "Alice")
student2 = Student(2, "Bob")

# Enroll students in courses
student1.enroll_course(course1)
student1.enroll_course(course2)
student2.enroll_course(course1)

# Assign grades
student1.assign_grade("CS101", 85)
student1.assign_grade("ENG201", 90)
student2.assign_grade("CS101", 75)

# Calculate GPA
print(f"{student1.name}'s GPA: {student1.calculate_gpa()}")
print(f"{student2.name}'s GPA: {student2.calculate_gpa()}")
