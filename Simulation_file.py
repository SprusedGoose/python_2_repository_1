 # simulation file

from LinkedList import *
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

        self.students = Student.generate_students(17)

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

