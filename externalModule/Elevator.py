class Elevator:
    occupant_limit = 8
    max_floors = 50
    min_floors = -5

    def __init__(self, curr_occupants, curr_floor):
        curr_floor = 0
        curr_occupants = 0

    def add_occupants(self, no_of_occupants):
        if (self.curr_occupant + no_of_occupants > Elevator.occupant_limit):
            print('Overcapacity')
        else:
            self.curr_occupant += no_of_occupants
            print('number of occupants are', Elevator.curr_occupant)

    def go_to_floor(self, floor_number):
        if (
                floor_number > Elevator.max_floors or
                floor_number < Elevator.min_floors):
            print('No such floor exists')
        else:
            Elevator.curr_floor += floor_number
            print('Current floor is', Elevator.curr_floor)


Elevator
e1 = Elevator()
e1.add_occupants(2)
e1.add_occupants(7)
e1.go_to_floor(-4)
