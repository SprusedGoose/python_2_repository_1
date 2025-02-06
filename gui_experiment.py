"""
This is a graphical user interface to run the simulation for the college sign.
"""

import customtkinter as tk
from tkinter import PhotoImage
from customtkinter import CTkLabel
from utilities import path


class Gui(tk.CTk):
    def __init__(self):
        super().__init__()
        # create a window
        self.resizable(width=False, height=False)

        self.frames = [
            # takes the file path of the gif and gives an index within the PhotoImage
            PhotoImage(file=path("wiz2.gif"), format="gif -index %i" % (i))
            # runs through the 182 frames of the image, making the animation work
            for i in range(182)
        ]

        # aliases the word label with the Label function in tkinter
        self.animation_label = CTkLabel(self)
        # packs the label function
        self.animation_label.grid(row=0, column=1)

        self.title("College sign simulator")

        # creates a text label for a checkbox
        # randomized_slides_label = tk.Label(window, text="Randomized slide order")
        # randomized_slides_label.pack()

        # slider and checkbox were modified from codemy.com youtube channel
        # third column
        randomized_slide_checkbox = tk.CTkSwitch(self, text="Randomize slide order", onvalue=1, offvalue=0, command=self.functions)
        randomized_slide_checkbox.grid(row=1, column=2)

        speeding_drivers_checkbox = tk.CTkSwitch(self, text="allow speeding drivers", onvalue=1, offvalue=0, command=self.speeding_drivers)
        speeding_drivers_checkbox.grid(row=2, column=2)

        maximum_speed = tk.CTkEntry(self, width=150)
        maximum_speed.grid(row=4, column=2)

        maximum_speed_label = tk.CTkLabel(self, text='enter maximum speed')
        maximum_speed_label.grid(row=3, column=2)

        speed_variation = tk.CTkEntry(self, width=150)
        speed_variation.grid(row=6, column=2)

        speed_variation_label = tk.CTkLabel(self, text='driver speed variation')
        speed_variation_label.grid(row=5, column=2)

        # second column
        slide_duration = tk.CTkSlider(self, fg_color='blue', from_=0, to=30, number_of_steps=30, command=self.slide_time_duration)
        slide_duration.grid(row=2, column=1)

        slide_duration_label = tk.CTkLabel(self, text=f"slide duration: {int(slide_duration.get())} seconds")
        slide_duration_label.grid(row=1, column=1)

        slide_count = tk.CTkSlider(self, fg_color='blue', from_=0, to=30, number_of_steps=30, command=self.slider_count)
        slide_count.grid(row=4, column=1)

        slide_count_label = tk.CTkLabel(self, text=f" slide count: {slide_count.get()} ")
        slide_count_label.grid(row=3, column=1)

        # speed bump settings
        speed_bump_slider = tk.CTkSlider(self, fg_color='blue', from_=0, to=4, number_of_steps=4, command=self.speed_bump_quantity_value)
        speed_bump_slider.grid(row=2, column=0)

        speed_bump_label = tk.CTkLabel(self, text=f"speed bump quantity: {speed_bump_slider.get()}")
        speed_bump_label.grid(row=1, column=0)

        speed_bump_height = tk.CTkSlider(self, fg_color='blue', from_=0, to=6, number_of_steps=6, command=self.speed_bump_height_value)
        speed_bump_height.grid(row=4, column=0)

        speed_bump_height_label = tk.CTkLabel(self, text=f"speed bump height: {speed_bump_height.get()} inches")
        speed_bump_height_label.grid(row=3, column=0)

        speed_bump_distance = tk.CTkSlider(self, fg_color='blue', from_=0, to=6, number_of_steps=6, command=self.speed_bump_spacing)
        speed_bump_distance.grid(row=6, column=0)

        speed_bump_distance_label = tk.CTkLabel(self, text=f"speedbump distance: {speed_bump_distance.get()} units")
        speed_bump_distance_label.grid(row=5, column=0)

        # sign viewing settings
        viewing_distance = tk.CTkEntry(self, width=150)
        viewing_distance.grid(row=6, column=1)

        view_dist = tk.CTkLabel(self, text="viewing distance")
        view_dist.grid(row=5, column=1)

        school_start = tk.CTkEntry(self, width=150)
        school_start.grid(row=8, column=1)

        school_start_label = tk.CTkLabel(self, text='school start time 24h')
        school_start_label.grid(row=7, column=1)

        school_end = tk.CTkEntry(self, width=150)
        school_end.grid(row=10, column=1)

        school_end_label = tk.CTkLabel(self, text='school end time 24h')
        school_end_label.grid(row=9, column=1)

        self.total_students_label = tk.CTkLabel(self, text='total enrolled students')
        self.total_students_label.grid(row=7, column=0)

        self.total_students = tk.CTkEntry(self, width=150)
        self.total_students.grid(row=8, column=0)

        self.dorm_students_label = tk.CTkLabel(self, text='total enrolled students')
        self.dorm_students_label.grid(row=9, column=0)

        self.dorm_students = tk.CTkEntry(self, width=150)
        self.dorm_students.grid(row=10, column=0)

        self.appearance = tk.CTkSwitch(self, text='Dark Mode', onvalue=1, offvalue=0, command=self.change_appearance)
        self.appearance.grid(row=10, column=2)

        # creates a button to run the simulaton
        self.entry_button = tk.CTkButton(self, text='press to start simulation', command=self.run_sample)
        # packs the entry button to the gui
        self.entry_button.grid(row=11, column=1)

        self.output = tk.CTkLabel(self, text='')
        self.output.grid(row=12, column=1)

    # taken and modified from stackoverflow
    # creates a function called update
    def update(self, ind):
        """
        This function uses an if statement that runs in an odd recursive loop to continuously update the framerate.
        It does this by increasing the frame value and the if statement resets the value if it is over 59, causing it to start over again.
        """

        # sets the frame to be at the frame at ind
        frame = self.frames[ind]
        # adds 1 to the value ind
        ind += 1

        # With this condition it will play gif infinitely
        # if the framerate is greater than 59, the frame is set back to 0
        if ind > 181:
            ind = 0
            # configures the image for the current frame
        self.animation_label.configure(image=frame, text='')
        # after the duration of update speed, the frame changes
        self.after(60, self.update, ind)

    # creates a dark mode function
    def change_appearance(self):
        value = self.appearance.get()
        if value == 1:
            tk.set_appearance_mode("dark")
        else:
            tk.set_appearance_mode("light")

    # adds textbox for setting maximum driver speed
    def speeding_drivers(self):
        speeding = self.speeding_drivers_checkbox.get()
        if (speeding == 1):
            speed_excess = True
            return speed_excess
        else:
            speed_excess = False
            return speed_excess

    # a function that does nothing
    def functions(self):
        """
        this function does absolutely nothing

        """
        pass

    # a function that is supposed to run a simulation
    def run_sample(self):
        """
        same goes for this function

        """
        self.values = {
            "speed_bump_quantity": self.speed_bump_slider.get(),
            "speed_bump_height": self.speed_bump_height.get(),
            "slide_duration": self.slide_duration.get(),
            "slide_count": self.slide_count.get(),
            "speed_bump_spacing": self.speed_bump_distance.get(),
            "viewing_distance": self.viewing_distance.get(),
            "school_start": self.school_start.get(),
            "school_end": self.school_end.get(),
            "total_students": self.total_students.get(),
            "dorm_students": self.dorm_students.get(),
            "speed_excess": self.speeding_drivers()
        }
        pass

    # starts the animation
        self.after(0, self.update, 0)

    def speed_bump_quantity_value(self, value):
        speed_bump = tk.CTkLabel(self, text=f"speed bump quantity: {value}")
        speed_bump.grid(row=1, column=0)

    def speed_bump_height_value(self, value):
        speed_bump_tallness = tk.CTkLabel(self, text=f"speed bump height: {value} inches")
        speed_bump_tallness.grid(row=3, column=0)

    def slide_time_duration(self, value):
        slide_time = tk.CTkLabel(self, text=f"slide duration: {value} seconds")
        slide_time.grid(row=1, column=1)

    def speed_bump_spacing(self, value):
        speed_bumps_spacing = tk.CTkLabel(self, text=f"speedbump distance: {value} units")
        speed_bumps_spacing.grid(row=5, column=0)

    def slider_count(self, value):
        slide_quantity = tk.CTkLabel(self, text=f"slide count: {value}")
        slide_quantity.grid(row=3, column=1)


if __name__ == "__main__":
    # creates a window
    window = Gui()
    window.after(0, window.update, 0)
    # runs the gui window in a loop
    window.mainloop()
