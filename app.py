from person import Person
from bus import Bus
from bus_stop import BusStop

# PART A
bus1 = Bus(1, "Brunswick Road")

print(f"the bus has left.{bus1.drive()}")

# PART B
initial_passengers = bus1.passenger_number_check()
print(f"there are initially {initial_passengers} passengers on the bus")

bus1.pick_up("John")
print(bus1.passengers)

passengers_currently_on_bus = (bus1.passenger_number_check())
print(f"there are currently {passengers_currently_on_bus} passengers on the bus")

bus1.drop_off("John")

bus1.empty()

# PART C

bus_stop1 = BusStop("King's Road")

bus_stop1.queue_clear()
print(len(bus_stop1.queue))

print(bus_stop1.queue)

bus1.pick_up_from_stop(bus_stop1)
