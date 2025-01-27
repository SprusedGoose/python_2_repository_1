"""
this is an experimental custom gui for the group project
"""

import customtkinter as tk
from tkinter import PhotoImage
from customtkinter import CTkLabel
from utilities import path


window = tk.CTk()

frames = [
    # takes the file path of the gif and gives an index within the PhotoImage
    PhotoImage(file=path("thing.gif"), format="gif -index %i" % (i))
    # runs through the 60 frames of the image, making the animation work
    for i in range(60)
]


def change_appearance():
    value = appearance.get()
    if value == 1:
        tk.set_appearance_mode("dark")
    else:
        tk.set_appearance_mode("light")


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
    if ind > 59:
        ind = 0
        # configures the image for the current frame
    label.configure(image=frame)
    # after the duration of update speed, the frame changes
    window.after(40, update, ind)


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


appearance = tk.CTkSwitch(window, fg_color="#82EEFD", border_color='#fdff99', text='Dark Mode', onvalue=1, offvalue=0, command=change_appearance)

appearance.grid(row=1, column=0)

# creates a button to run the simulaton
entry_button = tk.CTkButton(window, fg_color='blue', hover_color='turquoise', border_color='white', text='press to start simulation', command=run_sample)
# packs the entry button to the gui
entry_button.grid(row=2, column=2)

randomized_slides = tk.CTkSwitch(window, border_color='white', text='randomized slides', command=functions)
randomized_slides.grid(row=1, column=2)

speedbumps = tk.CTkSlider(window, fg_color='blue', from_=0, to=5, number_of_steps=5)
speedbumps.grid(row=1, column=1)

# runs the gui window in a loop
window.mainloop()
