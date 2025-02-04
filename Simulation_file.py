 # simulation file

import LinkedList
#from gui_experiment import *
import Student


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
    
    ):  
        
        # initialize students and slides
        self.students = Student.generate_students(17)
        
        self.sign = LinkedList.create_slides(20)

    # def check_slide_visabilty(self, SlideNode, time_range, day):
    #     if self.schedule[day] in range[time_range]:
            
    #         duration = time_range[1] - self.schedule[day] 
            
    #         self.view_slide(SlideNode, duration)

    def check_slide_visabilty(self, SlideNode, time_range, day):
    if self.schedule[day] in range[time_range]:
        
        duration = time_range[1] - self.schedule[day] 
        
        self.view_slide(SlideNode, duration)

    
    def simulate_sign_viewing(self):
        time = 0
        while time in range(simulation_span):
            time = time + self.slide_duration
            
            
            check_slide_visabilty(self.sign, time, 0)
            self.sign





    def say_hello(self):
        print(self.students)


    
    
    


if __name__ == "__main__":
    sim = simulation(0,0,0,0,0,0,0,0,0)
    sim.say_hello()

        

    


    
    



        



























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

