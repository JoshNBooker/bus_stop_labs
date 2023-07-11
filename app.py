from person import Person
from bus import Bus

bus1 = Bus(1, "Brunswick Road")

print(bus1.passenger_number_check())

bus1.pick_up("John")
print(bus1.passengers)

print(bus1.passenger_number_check())

bus1.pick_up("Mary")

bus1.drop_off("John")

print(bus1.passenger_number_check())
