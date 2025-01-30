import random
from schedule import daily_schedule  # Assuming this is the correct import

day_start = 9
day_end = 14

dorm_residents = 144
enrolled_students = 2132

class Student:
    def __init__(self):

        self.seen_slides = []
        
        self.lives_in_dorm = (random.randint(0, enrolled_students) < dorm_residents)
        self.schedule = [daily_schedule(0, 0)] * 7

        # Extend dorm resident schedule

        # Sign turns off at 10
        
        # Generate schedule for dorm residents
        if self.lives_in_dorm == True:
            for x in range(1, 6):
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


    # this method adds slides scene advents to slides scene list
    def view_slide(self, slide: SlideNode, duration):
        self.seen_slides.append([SlideNode, duration])

    def check_if_slide_student(self, slide: SlideNode, time_range, day):
        if self.schedule[day] in range[time_range]:
            
            duration = time_range[1] - self.schedule[day] 
            
            self.view_slide(SlideNode, duration)

if __name__ == "__main__":
    test_student = Student()

    print(test_student.schedule)



nominal_sign_viewing_time = 60
nominal_speed = 25
actual_speed = 20

division_from_nominal_speed_factor = actual_speed / nominal_speed

actual_sign_viewing_time = nominal_sign_viewing_time / division_from_nominal_speed_factor