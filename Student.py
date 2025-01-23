import random
from sqedual import daily_sqedual

day_start = 9
day_end = 14

dorm_residents = 144
enrolled_students = 2132

class Student:
    def __init__(self):

        self.seen_slides = {}
        
        self.lives_in_dorm = (random.randint(0,enrolled_students) < dorm_residents)
        self.sqedual = [daily_sqedual(0, 0)] * 7

        # exstend dorm resident schedaul

        # sign turns off at 10
        
        #Genarate sqedual for dorm residents
        if self.lives_in_dorm == True:
            for x in range(1,6):
                minminimum_day_length = 1
                arival_time = random.randint(day_start, day_end - minminimum_day_length)
                departure_time = random.randint(arival_time + minminimum_day_length, day_end)
                
                self.sqedual[x] = daily_sqedual(arival_time, departure_time)

        #Genarate sqedual for non dorm residents
        else:
            for x in range(0,7):
                if random.randint(0,2) == 1:
                    minminimum_day_length = 1
                    arival_time = random.randint(day_start, day_end - minminimum_day_length)
                    departure_time = random.randint(arival_time + minminimum_day_length, day_end)
                    
                    self.sqedual[x] = daily_sqedual(arival_time, departure_time)

    
    def say_hello(self):
        pass 

    def check_slide_visabilty(self, slide: SlideNode):
        pass



if __name__ == "__main__":
    test_student = Student()

    print(test_student.sqedual)