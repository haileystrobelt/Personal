from professor import Professor
from enroll import Enroll

class Course:
    def __init__(self, name, code, max_, min_, professor):
        self.name = name
        self.code = code
        self.max = max_
        self.min = min_
        self.professor = []
        self.enrollments = []

    if isinstance(professor, Professor):
        self.professors.append(professor)
    elif isinstance(professor, list):
        for entry in professor:
            if not isinstance(entry, Professor):
                raise Error("Invalid professor...")

        self.professors = professor
    else:
        raise Error("Invalid professor...")

    def add_professor(self, professor):
        if not isinstance(professor, Professor):
            raise Error("Invalid profesor...")

        self.professor.append(professor)

    def add_enrollment(self, enroll):
        if not isinstance(enroll.Enroll):
            raise Error("Invalid enroll...")

        if len(enrollments) == self.max:
            raise Error("Cannot enroll, course is full.")

        self.enrollments.append(enroll)

    def is_cancelled(self):
        return len(self.enrollments) <= self.min
