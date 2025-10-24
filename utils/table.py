# Seat class
# Represents a seat with two attributes:
# - free: a boolean indicating if the seat is available (default is True)
# - occupant: a string representing the person occupying the seat (default is None)
class Seat:
    def __init__(self, free=True, occupant=None) ->None:
        self.free = free
        self.occupant = occupant

    # Assigns a person to the seat if it is free and prints a confirmation message
    # If the seat is already occupied, prints a message indicating who is occupying it
    def set_occupant(self, name) ->None:
        if self.free:
            self.occupant = name
            self.free = False
            print(f"{name} assigned")
        else:
            print(f"Seat already occupied by {self.occupant}")

    # Removes the occupant from the seat and returns the occupant's name
    # If the seat is already free, returns None
    def remove_occupant(self) ->str:
        occupant_name = self.occupant
        self.occupant = None
        self.free = True
        return occupant_name
    
# Table class with two attributes:
# - capacity which is integer
# - seats which is a list of Seat objects (size = capacity)
class Table:
    def __init__(self, capacity:int, seats:list):
        self.capacity = capacity
        self.seats = [Seat() for i in range(capacity)]

    # Returns a boolean (True if a free spot is available)
    def has_free_spot(self) ->bool:
        # Loop through each seat in the table
        for seat in self.seats:
            if seat.free:
                print("Seat available at the table")
                return True
        print("No seat available at the table")
        return False

    # Places someone at the table
    def assign_seat(self, name) ->str:
        for seat in self.seats:
            if seat.free:
                seat.set_occupant(name)
                return name
        print("No seat available at the table\n")
        return None

    # Returns capacity left at a table
    def left_capacity(self) ->int:
        free_seat_counter = 0
        for seat in self.seats:
            if seat.free:
                free_seat_counter += 1
        # print(free_seat_counter)
        return free_seat_counter