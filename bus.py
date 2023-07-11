class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    
    def drive():
        return "Brum brum"
    
    def passenger_number_check(self):
        return len(self.passengers)
    
    def pick_up(self, passenger_name):
        self.passengers.append(passenger_name)

    def drop_off(self, passenger_name):
        self.passengers.remove(passenger_name)
