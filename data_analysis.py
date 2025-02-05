"""Data Analysis"""

from random import randint


def generate_slides(slide_count, slide_duration, slide_events):
    slides_seen = []
    for i in range(slide_events):
        slide_read = (randint(1, slide_count), randint(1, slide_duration))
        slides_seen.append(slide_read)
    return slides_seen


# creates a class student
class student:
    def __init__(self, view_events):
        self.view_events = view_events
        # Uses a set to track unique slides seen by the student, discarding any duplicates
        self.slides_seen = set()


# creates an empty list called students to contain the students and what slides they saw
students = []

# Creates 100 random students with random slide events (Carmine did this part to help me test it)
for x in range(100):
    students.append(student(generate_slides(20, 20, 10)))


# everything beyond this point is used for data analysis, all of the above is just to test it.
def analyze_slide_viewing(list_of_students):
    """
    this function takes a list of students along with the tuples that give what signs they saw and what duration they saw it.
    it then uses a dictionary to track how many slides have been seen overall

    """

    # Initializes a dictionary to track how many students saw each slide (1 to 20)
    slide_view_count = {i: 0 for i in range(1, 21)}

    # Loop through each student and their view events
    for student in list_of_students:
        for event in student.view_events:
            # aliases slide to the slide index number
            slide = event[0]
            # if the slide is viewed for more than 2 seconds, it registers that the student saw the slide
            if event[1] > 2:
                student.slides_seen.add(slide)

    # runs another nested for loop to add the viewed slide count to check how many times the slide has been seen
    for student in list_of_students:
        for slide in student.slides_seen:
            slide_view_count[slide] += 1

    # creates a value for unique slides and sets it to 0
    total_unique_slides = 0
    # finds the number of students there are by checking the length of the list
    total_students = len(list_of_students)

    # runs another for loop to get the total number of specific slides seen by each student
    for student in list_of_students:
        total_unique_slides += len(student.slides_seen)

    # finds the average number of slides seen across all of the students.
    # It does this by dividing how many slides every student saw together and divides it by the amount of students
    average_unique_slides = total_unique_slides / total_students if total_students > 0 else 0

    return f"\nthe students see {average_unique_slides:.2f} slides on average"


if __name__ == "__main__":
    # tells the program to Analyze how many students saw each slide and calculate the average number of slides seen by a student
    print(analyze_slide_viewing(students))
