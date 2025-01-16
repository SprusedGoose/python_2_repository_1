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

# creates a label for an status message
status_label = tk.Label(window)
# packs the message
status_label.pack()



# runs the gui window in a loop
window.mainloop()
