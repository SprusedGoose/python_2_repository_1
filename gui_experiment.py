"""
This is a graphical user interface to run the simulation for the college sign.
"""
from main import Main as sim
import customtkinter as tk
from tkinter import PhotoImage
from customtkinter import CTkLabel
from utilities import path

# <<<<<<< data_analysis
# =======
# button_values = None  # Initialize as a global variable

# >>>>>>> main


# creates a class called Gui that creates a graphical user interface
class Gui(tk.CTk):
    """
    This class handles creating a user interface application that takes inputs through sliders checkboxes and entry boxes
    """
    # creates an init method
    def __init__(self):
        """
        this initializes the class and sets the inputs and labels
        """
        super().__init__()
        # creates a fixed size for the gui
        self.resizable(width=False, height=False)

        self.frames = [
            # takes the file path of the gif and gives an index within the PhotoImage
            PhotoImage(file=path("wiz2.gif"), format="gif -index %i" % (i))
            # runs through the 182 frames of the image, making the animation work
            for i in range(182)
        ]

        # creates a label to contain the animation. (its a bit hacky because it's a tkinter animation in a customtkinter label)
        self.animation_label = CTkLabel(self)
        # puts the animation label into the grid of the gui
        self.animation_label.grid(row=0, column=1)
        # names the gui window
        self.title("College sign simulator")

        # slider and checkbox were modified from codemy.com youtube channel
        # creates a switch to control the randomized slides that triggers the functions method
        randomized_slide_checkbox = tk.CTkSwitch(self, text="Randomize slide order", onvalue=1, offvalue=0, command=self.functions)
        # puts the randomized slide switch into the window
        randomized_slide_checkbox.grid(row=1, column=2)
        # assigns the switch to self
        self.randomized_slide_checkbox = randomized_slide_checkbox

        # creates a speeding drivers switch (I really should have renamed it)
        speeding_drivers_checkbox = tk.CTkSwitch(self, text="allow speeding drivers", onvalue=1, offvalue=0, command=self.speeding_drivers)
        # puts the switch into the window
        speeding_drivers_checkbox.grid(row=2, column=2)
        # assigns the switch to self, not sure if necessary, but I did it anyway
        self.speeding_drivers_checkbox = speeding_drivers_checkbox

        # creates a base value of 5 for the entry box
        # (Carmine didn't end up needing it in the end but I didn't realized until later. I left it in for symetry)
        speed_val = tk.StringVar()
        speed_val.set("5")
        # creates an entry box to enter the speed variation with the initial value above
        speed_variation = tk.CTkEntry(self, width=150, textvariable=speed_val)
        # adds the entry into the window
        speed_variation.grid(row=8, column=2)
        self.speed_variation = speed_variation

        # creates a label to explain the previous entry box and adds it into the window
        speed_variation_label = tk.CTkLabel(self, text='driver speed variation')
        speed_variation_label.grid(row=7, column=2)
        self.speed_variation_label = speed_variation_label

        # creates a slider for setting the slide duration and activates a method to get its value
        slide_duration = tk.CTkSlider(self, fg_color='blue', from_=0, to=30, number_of_steps=30, command=self.slide_time_duration)
        # adds the slider into the window
        slide_duration.grid(row=2, column=1)
        self.slide_duration = slide_duration

        # creates a label to explain the previous slider and prints the value with its units
        slide_duration_label = tk.CTkLabel(self, text=f"slide duration: {int(slide_duration.get())} seconds")
        # adds the label into the window
        slide_duration_label.grid(row=1, column=1)
        self.slide_duration_label = slide_duration_label

        # creates a slider for setting the slide count and activates a method to get its value
        slide_count = tk.CTkSlider(self, fg_color='blue', from_=0, to=30, number_of_steps=30, command=self.slider_count)
        # adds the slider into the window
        slide_count.grid(row=4, column=1)
        self.slide_count = slide_count

        # creates a label to explain the slider for the slide count
        slide_count_label = tk.CTkLabel(self, text=f" slide count: {slide_count.get()} ")
        # adds the label into the window
        slide_count_label.grid(row=3, column=1)
        self.slide_count_label = slide_count_label

        # creates a slider for setting the simulation duration and activates a method to get its value
        simulation_duration = tk.CTkSlider(self, fg_color='blue', from_=1, to=26, number_of_steps=25, command=self.simulation_time_duration)
        # adds the slider into the window
        simulation_duration.grid(row=4, column=2)
        self.simulation_duration = simulation_duration

        # creates a label that explains the simulation duration label and displays its current value
        simulation_duration_label = tk.CTkLabel(self, text=f"simulation duration: {int(simulation_duration.get())} days")
        # adds the label into the window
        simulation_duration_label.grid(row=3, column=2)
        self.simulation_duration_label = simulation_duration_label

        # creates a slider for setting the speed bump quantity and activates a method to get its value
        speed_bump_slider = tk.CTkSlider(self, fg_color='blue', from_=0, to=4, number_of_steps=4, command=self.speed_bump_quantity_value)
        # adds the slider into the window
        speed_bump_slider.grid(row=2, column=0)
        self.speed_bump_slider = speed_bump_slider

        # creates a label for the speed bump quantity slider and prints its current value
        speed_bump_label = tk.CTkLabel(self, text=f"speed bump quantity: {speed_bump_slider.get()}")
        # adds the label to the window
        speed_bump_label.grid(row=1, column=0)
        self.speed_bump_label = speed_bump_label

        # creates a slider for setting the speed bump height and activates a method to get its value
        speed_bump_height = tk.CTkSlider(self, fg_color='blue', from_=0, to=6, number_of_steps=6, command=self.speed_bump_height_value)
        # adds the slider into the window
        speed_bump_height.grid(row=4, column=0)
        self.speed_bump_height = speed_bump_height

        # creates a label for the speed bump height slider and prints its current value
        speed_bump_height_label = tk.CTkLabel(self, text=f"speed bump height: {speed_bump_height.get()} inches")
        # adds the label into the window
        speed_bump_height_label.grid(row=3, column=0)
        self.speed_bump_height_label = speed_bump_height_label

        # creates an initial value for viewing duration
        view_dur_val = tk.StringVar()
        view_dur_val.set("20")
        # creates an entry box that contains an initial value
        viewing_duration = tk.CTkEntry(self, width=150, textvariable=view_dur_val)
        # adds the entry box to the window
        viewing_duration.grid(row=6, column=1)
        self.viewing_duration = viewing_duration

        # creates a label for the viewing duration entry box
        view_duration = tk.CTkLabel(self, text="viewing duration")
        # adds the label into the window
        view_duration.grid(row=5, column=1)
        self.view_duration = view_duration

        # creates an initial value for the school_start entry box
        school_start_val = tk.StringVar()
        school_start_val.set("9")
        # creates an entry box that contains an initial value
        school_start = tk.CTkEntry(self, width=150, textvariable=school_start_val)
        # adds the entry box into the window
        school_start.grid(row=8, column=1)
        self.school_start = school_start

        # creates a label to explain the school_start entry box
        school_start_label = tk.CTkLabel(self, text='school start time 24h')
        # adds the label into the window
        school_start_label.grid(row=7, column=1)
        self.school_start_label = school_start_label

        # creates an initial balue for the school_end entry box
        school_end_val = tk.StringVar()
        school_end_val.set("17")
        # creates an entry box that contains an initial value
        school_end = tk.CTkEntry(self, width=150, textvariable=school_end_val)
        # adds the entry box into the window
        school_end.grid(row=10, column=1)
        self.school_end = school_end

        # creates a label to explain the school end entry box
        school_end_label = tk.CTkLabel(self, text='school end time 24h')
        # adds the label into the window
        school_end_label.grid(row=9, column=1)
        self.school_end_label = school_end_label

        # creates a label to explain the total students entry box
        self.total_students_label = tk.CTkLabel(self, text='total enrolled students')
        # adds the total students label to the window
        self.total_students_label.grid(row=7, column=0)
        self.total_students_label = self.total_students_label

        # creates an initial value for the total students entry
        total_students_val = tk.StringVar()
        total_students_val.set("2132")
        # creates an entry box that contains an initial value
        self.total_students = tk.CTkEntry(self, width=150, textvariable=total_students_val)
        # adds the total students entry box to the window
        self.total_students.grid(row=8, column=0)
        self.total_students = self.total_students

        # creates a label to explain the dorm students entry box
        self.dorm_students_label = tk.CTkLabel(self, text='dorm students')
        # adds the label to the window
        self.dorm_students_label.grid(row=9, column=0)
        self.dorm_students_label = self.dorm_students_label

        # creates an initial value for the dorm students entry box
        dorm_students_val = tk.StringVar()
        dorm_students_val.set(str(int(4 * 4 * 3 * 3.5)))
        # creates an entry box for the amount of dorm students with the initial value above
        self.dorm_students = tk.CTkEntry(self, width=150, textvariable=dorm_students_val)
        # adds the entry box into the window
        self.dorm_students.grid(row=10, column=0)
        self.dorm_students = self.dorm_students

        # creates a switch to enable dark mode
        self.appearance = tk.CTkSwitch(self, text='Dark Mode', onvalue=1, offvalue=0, command=self.change_appearance)
        # adds the dark mode switch into the window
        self.appearance.grid(row=10, column=2)

        # creates a button to run the simulaton
        self.entry_button = tk.CTkButton(self, text='press to start simulation', command=self.run_sample)
        # packs the entry button to the gui
        self.entry_button.grid(row=11, column=1)

        # creates a label to act as a placeholder for the output
        self.output = tk.CTkLabel(self, text='')
        self.output.grid(row=12, column=1)

    # this section and the update function are from a stackoverflow question and were modified to work properly.
    # all they do is make the gif animation work (I got this last semester)
    #  https://stackoverflow.com/questions/43770847/play-an-animated-gif-in-python-with-tkinter
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

    # creates a dark mode method
    def change_appearance(self):
        """
        This method takes the state of the appearance switch and allows the program to change between dark mode and light mode.
        """
        value = self.appearance.get()
        if value == 1:
            tk.set_appearance_mode("dark")
        else:
            tk.set_appearance_mode("light")

    # adds textbox for setting maximum driver speed
    def speeding_drivers(self):
        """
        this method interprets the switch for speeding drivers
        """
        speeding = self.speeding_drivers_checkbox.get()
        # if the value of the switch is 1, it returns true, otherwise it returns false
        if (speeding == 1):
            speed_excess = True
            return speed_excess
        else:
            speed_excess = False
            return speed_excess

    # a method that does nothing, we didn't end up needing it
    def functions(self):
        """
        this function does absolutely nothing, we didn't get around to it and it might be unnescessary

        """
        pass

    # This method takes the information from the gui and plugs it into the simulation
    def run_sample(self):
        global button_values
        """
        This method takes the information from the gui and plugs it into the simulation.
        It also checks if the user entered proper information into the entry boxes and highlights them if they are wrong

        """

        # takes the user input speed_variation and turns it red and prints an error if it fails,
        # otherwise it runs and turns it white/dark depending on the mode (wasn't used in the end)
        # try:
        #     speed_variation = float(self.speed_variation.get())
        #     self.speed_variation.configure(fg_color=('white', '#2F2F2F'))
        # except Exception as ex:
        #     self.speed_variation.configure(fg_color='red')
        #     print('error, enter a number value')
        #     print(ex)

        # takes the user input speed_variation and turns it red and prints an error if it fails,
        # otherwise it runs and turns it white/dark depending on the mode
        try:
            viewing_duration = float(self.viewing_duration.get())
            self.viewing_duration.configure(fg_color=('white', '#2F2F2F'))
        except Exception as ex:
            self.viewing_duration.configure(fg_color='red')
            print('error, enter a number value')
            print(ex)

        # takes the user input speed_variation and turns it red and prints an error if it fails,
        # otherwise it runs and turns it white/dark depending on the mode
        try:
            school_start = float(self.school_start.get())
            self.school_start.configure(fg_color=('white', '#2F2F2F'))
        except Exception as ex:
            self.school_start.configure(fg_color='red')
            print('error, enter a number value')
            print(ex)

        # takes the user input speed_variation and turns it red and prints an error if it fails,
        # otherwise it runs and turns it white/dark depending on the mode
        try:
            school_end = float(self.school_end.get())
            self.school_end.configure(fg_color=('white', '#2F2F2F'))
        except Exception as ex:
            self.school_end.configure(fg_color='red')
            print('error, enter a number value')
            print(ex)

        # takes the user input speed_variation and turns it red and prints an error if it fails,
        # otherwise it runs and turns it white/dark depending on the mode
        try:
            total_students = int(self.total_students.get())
            self.total_students.configure(fg_color=('white', '#2F2F2F'))
        except Exception as ex:
            self.total_students.configure(fg_color='red')
            print('error, enter a number value')
            print(ex)

        # takes the user input speed_variation and turns it red and prints an error if it fails,
        # otherwise it runs and turns it white/dark depending on the mode
        try:
            dorm_students = int(self.dorm_students.get())
            self.dorm_students.configure(fg_color=('white', '#2F2F2F'))
        except Exception as ex:
            self.dorm_students.configure(fg_color='red')
            print('error, enter a number value')
            print(ex)

        # gathers the values from the gui in the form of a dictionary
        self.values = {
                "speed_bump_quantity": self.speed_bump_slider.get(),
                "speed_bump_height": self.speed_bump_height.get(),
                "slide_duration": self.slide_duration.get(),
                "slide_count": int(self.slide_count.get()),
                "viewing_duration": viewing_duration,
                "school_start": school_start,
                "school_end": school_end,
                "total_students": total_students,
                "dorm_students": dorm_students,
                "speed_excess": self.speeding_drivers(),
                "simulation_duration": int(self.simulation_duration.get())
        }

        # aliases self.values to button_values
        button_values = self.values

        # sets main to run the simulation with the values
        main = sim(button_values)
        # sets output equal to the result of running the simulation
        output = main.run()
        # creates a label and prints out the result
        self.output_label = CTkLabel(self, text=output)
        self.output_label.grid(row=12, column=1)
        # updates the animation
        self.after(0, self.update, 0)

    # creates methods to update the value of the sliders to the labels
    def speed_bump_quantity_value(self, value):
        """
        This method updates the text for the speed bump slider
        """
        speed_bump = tk.CTkLabel(self, text=f"speed bump quantity: {value}")
        speed_bump.grid(row=1, column=0)

    def speed_bump_height_value(self, value):
        """
        This method updates the text for the speed bump height slider
        """
        speed_bump_tallness = tk.CTkLabel(self, text=f"speed bump height: {value} inches")
        speed_bump_tallness.grid(row=3, column=0)

    def slide_time_duration(self, value):
        """
        This method updates the text for the slide duration slider
        """
        slide_time = tk.CTkLabel(self, text=f"slide duration: {value} seconds")
        slide_time.grid(row=1, column=1)

    def slider_count(self, value):
        """
        This method updates the text for the slide count slider
        """
        slide_quantity = tk.CTkLabel(self, text=f"slide count: {value}")
        slide_quantity.grid(row=3, column=1)

    def simulation_time_duration(self, value):
        """
        This method updates the text for the simulation duration slider
        """
        simulation_duration = tk.CTkLabel(self, text=f"simulation duration: {value} days")
        simulation_duration.grid(row=3, column=2)


# if this is the main program being run, it sets the program in motion
if __name__ == "__main__":
    # creates a window
    window = Gui()
    window.after(0, window.update, 0)
    # runs the gui window in a loop
    window.mainloop()
