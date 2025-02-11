# simulation file

import random

import LinkedList
# rom gui_experiment import *
import Student
from queue import Queue


class simulation:
    def __init__(self,
        # randomized_slide_checkbox,
        # speeding_drivers_checkbox,
        # maximum_speed,
        slide_duration,
        slide_count,
        # speed_bump_slider,
        speed_bump_height,
        # speed_bump_distance,
        # run_sample,
        # run_time,
        viewing_duration,
        speed_bump_quantity,
        #speed_bump_spacing,
        #viewing_distance,
        school_start,
        school_end,
        total_students,
        dorm_students,
        speed_excess,
        simulation_duration,
    ):
        # self.randomized_slide_checkbox = randomized_slide_checkbox
        # self.speeding_drivers_checkbox = speeding_drivers_checkbox
        # self.maximum_speed = maximum_speed
        self.slide_count = slide_count
        self.slide_duration = int(slide_duration)
        # self.slide_count = slide_count
        # self.speed_bump_slider = speed_bump_slider
        # self.speed_bump_height = speed_bump_height
        # self.speed_bump_distance = speed_bump_distance
        # self.run_sample = run_sample
        # self.run_time = run_time
        self.viewing_duration = viewing_duration

        self.simulation_duration = int(simulation_duration)

        # initialize students and slides
        self.students = Student.generate_students(total_students, dorm_students, school_start, school_end)
        # print(f'students {self.students}')

        # for student in self.students:
        #     print(student.schedule[1].arival_time)

        self.sign = LinkedList.create_slides(self.slide_count)

        self.slide_queue = Queue()

        slides_list = self.sign.get_nodes()

        time = 0

        #self.view_duration = 20

        print("run")

        # add each days to cue
        for day in range(simulation_duration):
            # add days worth of slides to the queue

            # print(day)
            # time in seconds from start of day
            time = 0
            while (time < 24*60*60):
                for slide in slides_list:
                    self.slide_queue.put((slide, time, day))
                    time = time + self.slide_duration

        print("queue")

    def simulate_sign_viewing(self):
        while not self.slide_queue.empty():
            slide, time, day = self.slide_queue.get()
            for student in self.students:

                # convert sudent arival time in hours to seconds since day start
                student_starting_time = student.schedule[day%7].arival_time * 60*60 + random.randint(0, 5*60)
                # print(f'day: {day} student_id: {student.id} student: arival time{student.schedule[day%7].arival_time}')
                # print(f'compairing {student_arving_time} {time}')
                # print(student.schedule[day%7].arival_time * 60*60)

                if student_starting_time in range(time, time + self.slide_duration):
                    student.view_slide(slide.slide_id, time - student_starting_time + self.viewing_duration)


    # this should trigger the class to get the data from linked_lists and combine it into a single output for futher processing
    def get_output(self):
        #for student in self.students:
         #   print(student.seen_slides)

        #output = []
        #for student in self.students:
         #   for advents in student.seen_slides:
          #      output.append(advents)

        return self.students

    def say_hello(self):
        return self.students


if __name__ == "__main__":
    sim = simulation(0, 0, 0, 20, 0, 0, 0, 0, 0, 2, 20)

    sim.simulate_sign_viewing()
    sim.get_output()
    # sim.say_hello()

