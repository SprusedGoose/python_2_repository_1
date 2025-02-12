# Comments and docstrings added with the assistance of GitHub Copilot

class daily_schedule:
    """
    Class to represent a daily schedule with arrival and departure times.
    """
    def __init__(self, arival_time, departure_time):
        """
        Initialize the daily schedule with arrival and departure times.

        :param arival_time: The arrival time.
        :param departure_time: The departure time.
        """
        self.arival_time = arival_time
        self.departure_time = departure_time

    def __repr__(self):
        """
        Return a string representation of the daily schedule.

        :return: String representation of the arrival and departure times.
        """
        return f'{self.arival_time}, {self.departure_time}'
