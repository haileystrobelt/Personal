from person import Person
from course import Course

class Professor(Person):
    def __init__(self, first, last, dob, phone, address, salary):
        super().__init__(self, first, last, dob, phone, address)
        self.salary = salary
        self.courses = []
        self.got_raise = False #makes sure we can't get raise multiple times.

    def check_for_rasie(self):
        if len(self.courses) >= 4 and not self.got_raise:
            self.salary += 20000
            self.got_rasie = True

    def add_course(self, course):
        if not isinstance(course, Course)
            raise Error("Invalid Course...")

        self.courses.append(course)