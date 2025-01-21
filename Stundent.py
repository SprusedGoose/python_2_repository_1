import random

days = ["sunday", "monday", "tuesday", "wendsday", "thursday", "friday", "saterday"]

class Student:
    def __init__(self, name, speeding_tendancy, school_hours, start_time_hour, end_time_hour):
        
        self.sqedual[x] = {key: None for key in days}

        dorm_residants = 144
        enroled_students = 2132


        #true is student lives in dorm. This is important because dorm residace have a difrent relation ship with how the view the sign.
        lives_in_dorm = (random(0,enroled_students) < dorm_residants)

        #genarate weekday school sqedual for non dorm residants
        if lives_in_dorm == False:
            for x in range(1,6):
                #arival times in half hour incroments
                self.sqedual[x] = random.randint(start_time_hour*2, end_time_hour*2) * 0.5

        for x in []

,
        #self.time_sign = 

        self.car_hieght = 5 # placeholder
        self.name = ""
        self.speeding_tendancy = speeding_tendancy
        self.slides_observation_duration = {} #{slide number : observation time}

