#main file for simulating

from LinkedList import *

from current_gui.py import(
    randomized_slide_checkbox as rndm,
    speeding_drivers_checkbox as spd,
    maximum_speed as maxspd,
    slide_duration as sld,
    slide_count as sldcnt,
    speed_bump_slider as spdbmp,
    speed_bump_height as spdbmpht,
    speed_bump_distance as spdbmpdst
)



# TEST CODE FOR SIM
import random

# unaffected view duration in seconds
view_duration = 60
slides_per_speed = 1

def simulate_sign_viewing(rndm, spd, maxspd, sld, sldcnt, spdbmp, spdbmpht, spdbmpdst):
    # Create the circular linked list of slides
    sign = CircularLinkedList()
    for slide_id in range(1, sldcnt + 1):
        sign.append(slide_id)

    # Randomize slides if needed
    if rndm:
        slides = list(range(1, sldcnt + 1))
        random.shuffle(slides)
        sign = CircularLinkedList()
        for slide_id in slides:
            sign.append(slide_id)

    # Set the speed bump if enabled, lowers speed by 1 mph
    if spdbmp:
        view_duration = 60 + int(spdbmp)*5
    


    



    # Simulate viewing
    total_viewed = []
    for day in range(student_days):
        daily_duration = max(0, random.gauss(view_duration, 5))  # Normal distribution for view time
        slides_seen = sign.display(daily_duration)
        total_viewed.extend(slides_seen)

    # Calculate unique slides seen
    unique_slides = set(total_viewed)
    percentage_seen = len(unique_slides) / num_slides * 100
    return percentage_seen, unique_slides

# Test Simulation
percentage, slides_seen = simulate_sign_viewing(randomize=True)
print(f"Percentage of slides seen: {percentage:.2f}%")
print(f"Slides seen: {sorted(slides_seen)}")
