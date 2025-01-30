class daily_sqedual:
    def __init__(self, arival_time, departure_time):
        self.arival_time = arival_time
        self.departure_time = departure_time

    def __repr__(self):
        return (f'{self.arival_time} {self.departure_time}')
