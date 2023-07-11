from person import Person
from bus import Bus
from bus_stop import BusStop

bus1 = Bus(1, "Brunswick Road")

print(f"the bus has left.{bus1.drive()}")

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

bus_stop1.queue_clear()
print(len(bus_stop1.queue))


bus_stop1.queue_add("Janie")

bus_stop1.queue_add("Fred")

print(bus_stop1.queue)

bus1.pick_up_from_stop(bus_stop1)
