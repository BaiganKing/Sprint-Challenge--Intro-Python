# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

#Base
class Vehicle():
    pass

#  [Vehicle]
#      |
#      v
# [GroundVehicle]
class GroundVehicle(Vehicle):
    pass

# [GroundVehicle]
#   |
#   v
# [Car]
class Car(GroundVehicle):
    pass

# [GroundVehicle]
#   |
#   v
# [Motorcycle]
class Motorcycle(GroundVehicle):
    pass

# [Vehicle]->[FlightVehicle]
class FlightVehicle(Vehicle):
    pass

# [FlightVehicle]
#   |
#   v
# [Airplane]
class Airplane(FlightVehicle):
    pass

# [Vehicle]->[FlightVehicle]->[Starship]
class Starship(FlightVehicle):
    pass
