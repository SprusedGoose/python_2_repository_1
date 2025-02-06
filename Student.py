import random


# daily schedule class not necicaly needed. this may be a good place to use a tuple -for carmine by carmine
from daily_schedule import daily_schedule

day_start = 8
day_end = 17

dorm_residents = 144
enrolled_students = 2132

def generate_students(number):    
    students = []
    for x in range(number):
        student = Student(x)
        student.genarate_schedule()
        students.append(student)

    return students


class Student:
    def __init__(self, id):

        self.id = id

        self.seen_slides = []
        
        # Randomly determine if student lives in dorm based on ratio of dorm residents to enrolled students
        self.lives_in_dorm = (random.randint(0, enrolled_students) < dorm_residents)
        self.schedule = [daily_schedule(0, 0)] * 7

        # Extend dorm resident schedule

        # Sign turns off at 10
        
        

    #this method adds slides scene advents to slides scene list
    def view_slide(self, SlideNode, duration):
        self.seen_slides.append((SlideNode, duration))

    def genarate_schedule(self):
        # Generate schedule for dorm residents
        if self.lives_in_dorm == True:
            for x in range(0, 7):
                minimum_day_length = 1
                arrival_time = random.randint(day_start, day_end - minimum_day_length)
                departure_time = random.randint(arrival_time + minimum_day_length, day_end)
                
                self.schedule[x] = daily_schedule(arrival_time, departure_time)

        # Generate schedule for non-dorm residents
        else:
            for x in range(0, 7):
                if random.randint(0, 2) == 1:
                    minimum_day_length = 1
                    arrival_time = random.randint(day_start, day_end - minimum_day_length)
                    departure_time = random.randint(arrival_time + minimum_day_length, day_end)
                    
                    self.schedule[x] = daily_schedule(arrival_time, departure_time)




if __name__ == "__main__":
    test_student = Student(1)

    test_student.genarate_schedule()

    print(test_student.schedule)



# nominal_sign_viewing_time = 60
# nominal_speed = 25
# actual_speed = 20

# division_from_nominal_speed_factor = actual_speed / nominal_speed

# actual_sign_viewing_time = nominal_sign_viewing_time / division_from_nominal_speed_factor