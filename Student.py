# Comments and docstrings added with the assistance of GitHub Copilot

import random
from daily_schedule import daily_schedule

def generate_students(enrolled_students, dorm_residents, day_start, day_end):
    """
    Function to generate a list of students.

    :param enrolled_students: Total number of enrolled students.
    :param dorm_residents: Number of dorm residents.
    :param day_start: Start time of the day.
    :param day_end: End time of the day.
    :return: List of generated students.
    """
    students = []
    for x in range(enrolled_students):
        student = Student(x, dorm_residents, enrolled_students)
        student.generate_schedule(day_start, day_end)
        students.append(student)
    return students

class Student:
    """
    Class to represent a student with a schedule and view events.
    """
    def __init__(self, id, dorm_residents, enrolled_students):
        """
        Initialize the student with an ID, dorm residency status, and schedule.

        :param id: Student ID.
        :param dorm_residents: Number of dorm residents.
        :param enrolled_students: Total number of enrolled students.
        """
        self.id = id
        self.view_events = []
        self.slides_seen = set()
        # Randomly determine if student lives in dorm based on ratio of dorm residents to enrolled students
        self.lives_in_dorm = (random.randint(0, enrolled_students) < dorm_residents)
        self.schedule = [daily_schedule(0, 0)] * 7

    def view_slide(self, SlideNode, duration):
        """
        Add a slide viewing event to the student's view events.

        :param SlideNode: The slide node being viewed.
        :param duration: Duration of the viewing event.
        """
        self.view_events.append((SlideNode, duration))

    def generate_schedule(self, day_start, day_end):
        """
        Generate a weekly schedule for the student.

        :param day_start: Start time of the day.
        :param day_end: End time of the day.
        """
        # Generate schedule for dorm residents
        if self.lives_in_dorm:
            for x in range(7):
                minimum_day_length = 1
                arrival_time = random.uniform(day_start, day_end - minimum_day_length)
                departure_time = random.uniform(arrival_time + minimum_day_length, day_end)
                self.schedule[x] = daily_schedule(arrival_time, departure_time)
        # Generate schedule for non-dorm residents
        else:
            for x in range(7):
                if random.randint(0, 2) == 1:
                    minimum_day_length = 1
                    arrival_time = random.uniform(day_start, day_end - minimum_day_length)
                    departure_time = random.uniform(arrival_time + minimum_day_length, day_end)
                    self.schedule[x] = daily_schedule(arrival_time, departure_time)

if __name__ == "__main__":
    test_student = Student(1, 5, 17)
    test_student.generate_schedule(5, 17)
    print(test_student.schedule)


