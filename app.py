from person import Person
from bus import Bus
from bus_stop import BusStop

bus1 = Bus(1, "Brunswick Road")

print(bus1.passenger_number_check())

bus1.pick_up("John")
print(bus1.passengers)

print(bus1.passenger_number_check())

bus1.pick_up("Mary")

bus1.drop_off("John")

print(bus1.passenger_number_check())

bus1.empty()
print(bus1.passenger_number_check())

bus_stop1 = BusStop("King's Road")

bus_stop1.queue_add("Janie")
print(len(bus_stop1.queue))