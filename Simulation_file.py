 # simulation file

import random

import LinkedList
#from gui_experiment import *
import Student

from queue import Queue
class simulation:
    def __init__(self,
        randomized_slide_checkbox, 
        speeding_drivers_checkbox, 
        maximum_speed,
        slide_duration,
        slide_count,
        speed_bump_slider,
        speed_bump_height,
        speed_bump_distance,
        run_sample,
        run_time,
        view_duration
    
    ):  
        self.randomized_slide_checkbox = randomized_slide_checkbox
        self.speeding_drivers_checkbox = speeding_drivers_checkbox
        self.maximum_speed = maximum_speed
        self.slide_duration = slide_duration
        self.slide_count = slide_count
        self.speed_bump_slider = speed_bump_slider
        self.speed_bump_height = speed_bump_height
        self.speed_bump_distance = speed_bump_distance
        self.run_sample = run_sample
        self.run_time = run_time
        self.view_duration = view_duration
 


        # initialize students and slides
        self.students = Student.generate_students(3)
       # print(f'students {self.students}')

        # for student in self.students:
        #     print(student.schedule[1].arival_time)
        
        self.sign = LinkedList.create_slides(3)

        self.slide_queue = Queue()

        slides_list = self.sign.get_nodes()

        time = 0

        view_duration = 20
        

        print("run")

        # add each days to cue
        for day in range(run_time):
            # add days worth of slides to the queue

            #print(day)

            time = 0 #time in seconds from start of day
            while(time < 24*60*60):
                for slide in slides_list:
                    self.slide_queue.put((slide, time, day))
                    time = time + self.slide_duration

        print("queue")

    def simulate_sign_viewing(self):
        while not self.slide_queue.empty():
            slide, time, day = self.slide_queue.get()
            for student in self.students:
                
                #convert sudent arival time in hours to seconds since day start
                student_starting_time = student.schedule[day%7].arival_time * 60*60 + random.randint(0, 5*60)
                #print(f'day: {day} student_id: {student.id} student: arival time{student.schedule[day%7].arival_time}')
                #print(f'compairing {student_arving_time} {time}')
                #print(student.schedule[day%7].arival_time * 60*60)


                
                
                if student_starting_time in range(time, time + self.slide_duration):
                    student.view_slide(slide, time - student_starting_time + self.view_duration)
 

    def get_output(self):
        # for student in self.students:
        #     print(student.seen_slides)

        output = []
        for student in self.students:
            for advents in student.seen_slides:
                output.append(advents)
            
        print(output)



    def say_hello(self):
        print(self.students)


if __name__ == "__main__":
    sim = simulation(0,0,0,20,0,0,0,0,0,2,20)
    
    sim.simulate_sign_viewing()
    sim.get_output()
    #sim.say_hello()

        

    


    
    



        



























# class Settings:
#     def __init__(self,
#                 randomized_slide_checkbox, 
#                 speeding_drivers_checkbox, 
#                 maximum_speed,
#                 slide_duration,
#                 slide_count,
#                 speed_bump_slider,
#                 speed_bump_height,
#                 speed_bump_distance,
#                 run_sample,


#                 ):
                
#         self.randomized_slide_checkbox = randomized_slide_checkbox
#         self.speeding_drivers_checkbox = speeding_drivers_checkbox   
#         self.maximum_speed = maximum_speed
#         self.slide_duration = slide_duration
#         self.slidecount = slide_count
#         self.speed_bump_slider = speed_bump_slider
#         self.speed_bump_height = speed_bump_height
#         self.speed_bump_distance = speed_bump_distance
#         self.run_sample = run_sample


# settings = Settings()
# gui = Gui(settings)

