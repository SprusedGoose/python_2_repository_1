from gui_experiment import Gui, button_values
import Simulation_file as sim

gui = Gui()

class Main():
    def __init__(self, settings):
        self.settings = settings

    def get_settings(self):
        global settings

        if __name__ == "__main__":
        # creates a window
            window = Gui()
            window.after(0, window.update, 0)
            # runs the gui window in a loop
            window.mainloop()
            
        while button_values is None:  # Wait until button_values is set
            pass
        settings = button_values  # Retrieve settings from GUI
        print(settings)
        
        

# Initialize settings with None before passing it to Main
settings = None
main = Main(settings)
# gui.after(0, gui.update, 0)
main.get_settings()
