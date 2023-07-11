from bus_stop import BusStop

class Bus:
    def __init__(self, route_number, destination):
        self.route_number = route_number
        self.destination = destination
        self.passengers = []
    
    def drive(bus):
        return " Brum brum"
    
    def passenger_number_check(self):
        return len(self.passengers)
    
    def pick_up(self, passenger_name):
        self.passengers.append(passenger_name)

    def drop_off(self, passenger_name):
        self.passengers.remove(passenger_name)
    
    def empty(self):
        self.passengers.clear()
    
    def pick_up_from_stop(self, BusStop):
        print(f"{BusStop.queue} are waiting")
        for passenger in BusStop.queue:
            self.passengers.append(passenger)
        BusStop.queue_clear()
        print(f"{self.passengers} have now boarded the bus")

