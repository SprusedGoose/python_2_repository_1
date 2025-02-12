# simulation file
# Comments and docstrings added with the assistance of GitHub Copilot

from collections import deque
import random
import LinkedList
# from gui_experiment import *
import Student

class simulation:
    """
    Simulation class to simulate sign viewing by students.
    """
    def __init__(self,
        slide_duration,
        slide_count,
        speed_bump_height,
        viewing_duration,
        speed_bump_quantity,
        school_start,
        school_end,
        total_students,
        dorm_students,
        speed_excess,
        simulation_duration,
    ):
        """
        Initialize the simulation with the given parameters.

        :param slide_duration: Duration of each slide.
        :param slide_count: Total number of slides.
        :param speed_bump_height: Height of speed bumps.
        :param viewing_duration: Duration for which a slide is viewed.
        :param speed_bump_quantity: Quantity of speed bumps.
        :param school_start: School start time.
        :param school_end: School end time.
        :param total_students: Total number of students.
        :param dorm_students: Number of dorm students.
        :param speed_excess: Speed excess value.
        :param simulation_duration: Duration of the simulation.
        """
        # Initialize parameter variables
        self.slide_count = slide_count
        self.slide_duration = int(slide_duration)
        self.viewing_duration = viewing_duration
        self.simulation_duration = int(simulation_duration)

        # Initialize students and sign
        self.students = Student.generate_students(total_students, dorm_students, school_start, school_end)
        self.sign = LinkedList.create_slides(self.slide_count)
        self.student_queue = deque()

        # Initialize time counter
        self.time = 0

    def simulate_sign_viewing(self):
        """
        Simulate the sign viewing process for the given duration.
        """
        print("run")

        # On every day
        for day in range(self.simulation_duration):
            # Run through all slides
            self.time = 0
            while self.time < 24 * 60 * 60:
                # Get current slide
                self.current_slide = self.sign.next_slide()
                
                # Add all students to the queue
                self.student_queue.extend(self.students)
                
                # Compare student visibility time to slide display time
                while len(self.student_queue) > 0:
                    student = self.student_queue.popleft()
                    student_starting_time = int(student.schedule[day % 7].arival_time * 60 * 60 + random.randint(0, 5 * 60))

                    if student_starting_time in range(self.time, self.time + self.slide_duration):
                        student.view_slide(self.current_slide.slide_id, self.time - student_starting_time + self.viewing_duration)
                
                # Increment time
                self.time += self.slide_duration

    def get_output(self):
        """
        Get the output of the simulation.

        :return: List of students with their view events.
        """
        return self.students

    def say_hello(self):
        """
        Dummy method to return students.

        :return: List of students.
        """
        return self.students

if __name__ == "__main__":
    sim = simulation(0, 0, 0, 20, 0, 0, 0, 0, 0, 2, 20)
    sim.simulate_sign_viewing()
    sim.get_output()
    # sim.say_hello()

