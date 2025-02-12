# Comments made with the assistance of GitHub Copilot

import Simulation_file as simulator
from data_analysis import analyze_slide_viewing

class Main():
    """
    Main class to run the simulation and analyze the output.
    """
    def __init__(self, settings):
        """
        Initialize the Main class with settings.

        :param settings: Dictionary containing simulation settings.
        """
        self.settings = settings

    def run(self):
        """
        Run the simulation and analyze the output.

        :return: Analyzed output of the simulation.
        """
        # Initialize the simulation with the provided settings
        sim = simulator.simulation(**self.settings)

        # Run the simulation
        sim.simulate_sign_viewing()

        # Get the simulation output
        sym_output = sim.get_output()

        # Analyze the simulation output
        output = analyze_slide_viewing(sym_output, self.settings['slide_count'])
        
        return output

# Initialize settings (to be defined)
settings = None

# Create an instance of Main with the settings
main = Main(settings)
