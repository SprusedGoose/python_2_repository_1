"""
This is a graphical user interface to run the simulation for the college sign.
"""

from tkinter import Label, PhotoImage
from utilities import path
import tkinter as tk

window = tk.Tk()


frames = [
    # takes the file path of the gif and gives an index within the PhotoImage
    PhotoImage(file=path("thing.gif"), format="gif -index %i" % (i))
    # runs through the 60 frames of the image, making the animation work
    for i in range(60)
]


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
label = Label(window)
# packs the label function
label.pack()
# sets the title of the window
window.title("College sign simulator")

# creates a text label for a checkbox
# randomized_slides_label = tk.Label(window, text="Randomized slide order")
# randomized_slides_label.pack()

var1 = bool

# slider and checkbox were modified from codemy.com youtube channel
randomized_slide_checkbox = tk.Checkbutton(window, text="Randomize slide order", variable=var1, onvalue=1, offvalue=0, command=functions)
randomized_slide_checkbox.pack()

speed_bump_slider = tk.Scale(window, from_=0, to=5, orient="horizontal")
speed_bump_slider.pack()

# creates a button to run the simulaton
entry_button = tk.Button(window, text='press to start simulation', command=run_sample)
# packs the entry button to the gui
entry_button.pack()

# runs the gui window in a loop
window.mainloop()
