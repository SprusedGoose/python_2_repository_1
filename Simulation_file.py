# simulation file

from collections import deque

import random

import LinkedList
# rom gui_experiment import *
import Student


class simulation:
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
        # ititialize parameter variables
        self.slide_count = slide_count
        
        self.slide_duration = int(slide_duration)

        self.viewing_duration = viewing_duration

        self.simulation_duration = int(simulation_duration)

        # Initilise students and sign
        self.students = Student.generate_students(total_students, dorm_students, school_start, school_end)
    
        print(self.slide_count)
        self.sign = LinkedList.create_slides(self.slide_count)

        self.student_queue = deque()

        # initilize time counter
        self.time = 0

    def simulate_sign_viewing(self):
        print("run")

        # on every day
        for day in range(self.simulation_duration):
            
            # run through all slides
            self.time = 0
            while (self.time < 24*60*60):
                # get curent slide
                self.current_slide = self.sign.next_slide()
                
                
                # add all students to the queue
                self.student_queue.extend(self.students)
                
                #compare student => visabilty time to slide display time
                while len(self.student_queue) > 0:                   
                    student = self.student_queue.popleft()
                    
                    
                    student_starting_time = int(student.schedule[day%7].arival_time * 60*60 + random.randint(0, 5*60))
                    #print(f'checking student start time:{student_starting_time} against curent time: {self.time}')
    

                    if student_starting_time in range(self.time, self.time + self.slide_duration):
                        student.view_slide(self.current_slide.slide_id, self.time - student_starting_time + self.viewing_duration)
                
                        print("slide seen<============")
                        #input()
                    
                        print(f'student {student.id} saw slide {self.current_slide.slide_id} at {self.time} \n the students schedule was {student.schedule}')
                        #print(self.current_slide)
                    
                    else:
                        pass
                        #print("slide not scene")
                    


                #incroment time
                self.time = self.time + self.slide_duration
                
                

                # This always gose last
                

    # # add each days to cue
    # for day in range(simulation_duration):
    #     # add days worth of slides to the queue

    #     # time in seconds from start of day
    #     time = 0
    #     while (time < 24*60*60):
    #         for slide in slides_list:
    #             self.slide_queue.put((slide, time, day))
    #             time = time + self.slide_duration

    print("queue")


        
        
        
        
        
        # while not self.slide_queue.empty():
        #     slide, time, day = self.slide_queue.get()
        #     for student in self.students:

        #         # convert sudent arival time in hours to seconds since day start
        #         student_starting_time = student.schedule[day%7].arival_time * 60*60 + random.randint(0, 5*60)

        #         if student_starting_time in range(time, time + self.slide_duration):
        #             student.view_slide(slide.slide_id, time - student_starting_time + self.viewing_duration)


    # this should trigger the class to get the data from linked_lists and combine it into a single output for futher processing
    def get_output(self):
        
        #for student in self.students:
            #print(f'{student.view_events} {student.schedule}  {student.id}')
        return self.students


    def say_hello(self):
        return self.students


if __name__ == "__main__":
    sim = simulation(0, 0, 0, 20, 0, 0, 0, 0, 0, 2, 20)

    sim.simulate_sign_viewing()
    sim.get_output()
    # sim.say_hello()

