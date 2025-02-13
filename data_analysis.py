"""Data Analysis"""
# import tkinter as tk
from random import randint
import tkinter as tk
from tkinter import Label
# from utilities import path


def generate_slides(slide_count, slide_duration, slide_events):
    """
    this generates random slide events for students to see
    """
    slides_seen = []
    for i in range(slide_events):
        slide_read = (randint(1, slide_count), randint(1, slide_duration))
        slides_seen.append(slide_read)
    return slides_seen


# creates a class student
class student:
    """
    this creates a class student for testing purposes, not used in the final program
    """
    def __init__(self, view_events):
        """
        initializes the class and assigns placeholders for lists and a set function to store unique slides
        """
        self.view_events = view_events
        # Uses a set to track unique slides seen by the student, discarding any duplicates
        self.slides_seen = set()


# everything beyond this point is used for data analysis, all of the above is just to test it.
def analyze_slide_viewing(list_of_students, slide_count):
    """
    this function takes a list of students along with the tuples that give what signs they saw and what duration they saw it.
    it then uses a dictionary to track how many slides have been seen overall

    """

    # Initializes a dictionary to track how many students saw each slide (1 to 20)
    slide_view_count = {i: 0 for i in range(1, 21)}

    # Loop through each student and their view events
    for student in list_of_students:
        # print(student.view_events)
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
    percentage_of_slides = round((average_unique_slides / slide_count)*100)

    # used for testing purposes
    # for slide, count in slide_view_count.items():
    #     print(f"Slide {slide} was seen by {count} students.")

    return f"\non average, the students see {average_unique_slides:.2f} or {percentage_of_slides}% of the total slides"


def output_data(student_list, slide_count):
    """
    this function creates a tkinter window to output the data from a randomly generated student list and prints the data to the window
    """

    # creates a window
    window = tk.Tk()

    # creates a label with the information and packs it to the tkinter window
    output_label = Label(window, text=analyze_slide_viewing(student_list, slide_count))
    output_label.pack()

    # runs the tkinter window
    window.mainloop()


# if this is the main program it runs this test section
if __name__ == "__main__":
    students = []
    slide_count = 20
    # Creates 100 random students with random slide events (Carmine did this part to help me test it)
    for x in range(100):
        students.append(student(generate_slides(slide_count, 20, 30)))
    # tells the program to Analyze how many students saw each slide and calculate the average number of slides seen by a student
    # analyze_slide_viewing(students)

    # runs the data analysis and prints to a gui
    output_data(students, slide_count)
