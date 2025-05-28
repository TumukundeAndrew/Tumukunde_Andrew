# Super class
class Person:
    def __init__(self, id_number, name):
        self.id_number = id_number
        self.name = name

    def display_info(self):
        print(f'ID {self.id_number}, Name: {self.name}, Role: Generic Person')

    def perform_action(self):
        print(f'{self.name} is performing a generic action.')

# Student
class Student(Person):
    def __init__(self, id_number, name, credits):
        super().__init__(id_number, name)
        self.credits = credits  # Store academic credits

    # Override display_info
    def display_info(self):
        print(f'ID {self.id_number}, Name: {self.name}, Role: Student, Credits: {self.credits}')

    # Add new method for enrolling in courses
    def enroll_course(self, course_credits):
        if course_credits > 0:
            self.credits += course_credits
            print(f'Enrolled in course worth {course_credits} credits. New total: {self.credits}')
        else:
            print('Invalid course credits.')

# Subclass: Lecturer
class Lecturer(Person):
    def __init__(self, id_number, name, courses_taught):
        super().__init__(id_number, name)
        self.courses_taught = courses_taught  # Store number of courses taught

    # Override display_info
    def display_info(self):
        print(f'ID {self.id_number}, Name: {self.name}, Role: Lecturer, Courses Taught: {self.courses_taught}')

    # Add new method for assigning courses
    def assign_course(self, course_count):
        if course_count > 0:
            self.courses_taught += course_count
            print(f'Assigned {course_count} course(s). Total courses taught: {self.courses_taught}')
        else:
            print('Invalid course count.')

# Subclass: Staff
class Staff(Person):
    def __init__(self, id_number, name, hours_worked):
        super().__init__(id_number, name)
        self.hours_worked = hours_worked  # Store hours worked

    # Override display_info
    def display_info(self):
        print(f'ID {self.id_number}, Name: {self.name}, Role: Staff, Hours Worked: {self.hours_worked}')

    # Override perform_action to reflect staff tasks
    def perform_action(self):
        if self.hours_worked >= 0:
            self.hours_worked += 8  # Assume a standard 8-hour task
            print(f'{self.name} completed a task. Total hours worked: {self.hours_worked}')
        else:
            print('Invalid hours worked.')

# Create objects
student = Student('STU123456', 'Alice Smith', 30)
lecturer = Lecturer('LEC789012', 'Dr. Bob Jones', 2)
staff = Staff('STF345678', 'Carol White', 40)

# Test methods
student.display_info()
student.enroll_course(6)
student.perform_action()
print(' LB ____________________')
lecturer.display_info()
lecturer.assign_course(1)
lecturer.perform_action()
print(' LB ____________________')
staff.display_info()
staff.perform_action()
staff.perform_action()
print(' LB ____________________')
print('MRO for Student:')
print(Student.__mro__)