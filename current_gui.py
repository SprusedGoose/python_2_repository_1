"""
This is a graphical user interface to run the simulation for the college sign.
"""

import customtkinter as tk
from tkinter import PhotoImage
from customtkinter import CTkLabel
from utilities import path


window = tk.CTk()

window.resizable(width=False, height=False)

frames = [
    # takes the file path of the gif and gives an index within the PhotoImage
    PhotoImage(file=path("wiz2.gif"), format="gif -index %i" % (i))
    # runs through the 60 frames of the image, making the animation work
    for i in range(182)
]


# taken and modified from stackoverflow
# creates a function called update
def update(ind):
    """
    This function uses an if statement that runs in an odd recursive loop to continuously update the framerate.
    It does this by increasing the frame value and the if statement resets the value if it is over 59, causing it to start over again.
    """

    # sets the frame to be at the frame at ind
    frame = frames[ind]
    # adds 1 to the value ind
    ind += 1

    # With this condition it will play gif infinitely
    # if the framerate is greater than 59, the frame is set back to 0
    if ind > 181:
        ind = 0
        # configures the image for the current frame
    label.configure(image=frame, text='')
    # after the duration of update speed, the frame changes
    window.after(60, update, ind)


# creates a dark mode function
def change_appearance():
    value = appearance.get()
    if value == 1:
        tk.set_appearance_mode("dark")
    else:
        tk.set_appearance_mode("light")


# adds textbox for setting maximum driver speed
def speeding_drivers():
    speeding = speeding_drivers_checkbox.get()
    if (speeding == 1):
        speed_excess = True
        return speed_excess
    else:
        speed_excess = False
        return speed_excess


# a function that does nothing
def functions():
    """
    this function does absolutely nothing

    """
    pass


# a function that is supposed to run a simulation
def run_sample():
    """
    same goes for this one

    """
    pass


# starts the animation
window.after(0, update, 0)


# aliases the word label with the Label function in tkinter
label = CTkLabel(window)
# packs the label function
label.grid(row=0, column=1)
# sets the title of the window
window.title("College sign simulator")

# creates a text label for a checkbox
# randomized_slides_label = tk.Label(window, text="Randomized slide order")
# randomized_slides_label.pack()


# slider and checkbox were modified from codemy.com youtube channel
# third column
randomized_slide_checkbox = tk.CTkSwitch(window, text="Randomize slide order", onvalue=1, offvalue=0, command=functions)
randomized_slide_checkbox.grid(row=1, column=2)

speeding_drivers_checkbox = tk.CTkSwitch(window, text="allow speeding drivers", onvalue=1, offvalue=0, command=speeding_drivers)
speeding_drivers_checkbox.grid(row=2, column=2)

maximum_speed = tk.CTkEntry(window, width=20)
maximum_speed.grid(row=4, column=2)

maximum_speed_label = tk.CTkLabel(window, text='enter maximum speed')
maximum_speed_label.grid(row=3, column=2)

speed_variation = tk.CTkEntry(window, width=20)
speed_variation.grid(row=6, column=2)

speed_variation_label = tk.CTkLabel(window, text='driver speed variation')
speed_variation_label.grid(row=5, column=2)

# second column
slide_duration = tk.CTkSlider(window, fg_color='blue', from_=0, to=5, number_of_steps=5)
slide_duration.grid(row=1, column=1)

slide_duration_label = tk.CTkLabel(window, text="slide duration")
slide_duration_label.grid(row=2, column=1)

slide_count = tk.CTkSlider(window, fg_color='blue', from_=0, to=5, number_of_steps=5)
slide_count.grid(row=3, column=1)

slide_count_label = tk.CTkLabel(window, text="slide count")
slide_count_label.grid(row=4, column=1)


# speed bump settings
speed_bump_slider = tk.CTkSlider(window, fg_color='blue', from_=0, to=5, number_of_steps=5)
speed_bump_slider.grid(row=1, column=0)

speed_bump_label = tk.CTkLabel(window, text="speed bump quantity")
speed_bump_label.grid(row=2, column=0)

speed_bump_height = tk.CTkSlider(window, fg_color='blue', from_=0, to=5, number_of_steps=5)
speed_bump_height.grid(row=3, column=0)

speed_bump_height_label = tk.CTkLabel(window, text="speed bump height")
speed_bump_height_label.grid(row=4, column=0)

speed_bump_distance = tk.CTkSlider(window, fg_color='blue', from_=0, to=5, number_of_steps=5)
speed_bump_distance.grid(row=5, column=0)

speed_bump_distance_label = tk.CTkLabel(window, text="length between speedbumps")
speed_bump_distance_label.grid(row=6, column=0)


# sign viewing settings
viewing_distance = tk.CTkEntry(window, width=20)
viewing_distance.grid(row=6, column=1)

viewing_distance_label = tk.CTkLabel(window, text="viewing distance")
viewing_distance_label.grid(row=5, column=1)

school_start = tk.CTkEntry(window, width=20)
school_start.grid(row=8, column=1)

school_start_label = tk.CTkLabel(window, text='school start time 24h')
school_start_label.grid(row=7, column=1)

school_end = tk.CTkEntry(window, width=20)
school_end.grid(row=10, column=1)

school_end_label = tk.CTkLabel(window, text='school end time 24h')
school_end_label.grid(row=9, column=1)

total_students_label = tk.CTkLabel(window, text='total enrolled students')
total_students_label.grid(row=7, column=0)

total_students = tk.CTkEntry(window, width=20)
total_students.grid(row=8, column=0)

dorm_students_label = tk.CTkLabel(window, text='total enrolled students')
dorm_students_label.grid(row=9, column=0)

dorm_students = tk.CTkEntry(window, width=20)
dorm_students.grid(row=10, column=0)

appearance = tk.CTkSwitch(window, fg_color="#82EEFD", border_color='#fdff99', text='Dark Mode', onvalue=1, offvalue=0, command=change_appearance)
appearance.grid(row=10, column=2)

# creates a button to run the simulaton
entry_button = tk.CTkButton(window, text='press to start simulation', command=run_sample)
# packs the entry button to the gui
entry_button.grid(row=11, column=1)

# runs the gui window in a loop
window.mainloop()
