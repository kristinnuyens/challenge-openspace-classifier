from table import Table, Seat
import random

# Create the class for OpenSpace with following attributes:
# tables which is a list of Table - import Table from table.py later
# number_of_tables which is an integer
class OpenSpace:
    def __init__(self, tables:list, number_of_tables:int):
        self.tables = [Table(4, []) for i in range(number_of_tables)]
        self.number_of_tables = number_of_tables

    # Create methods:
    # organize(names) that will randomly assign people to Seat objects in the different table objects
    def organize(self, new_colleagues) ->list:
        # shuffling the list for the random assignment
        shuffled_list = new_colleagues.copy()
        random.shuffle(shuffled_list)
        # added to check if the list was indeed shuffled
        print("Shuffled order:", shuffled_list)
        # assign each new colleague to a seat
        for new_colleague in shuffled_list:
            seat_assigned = False
            for table in self.tables:
                if table.assign_seat(new_colleague):
                    seat_assigned = True
                    break

    # display() to display the different tables and their occupants in a nice and readable way
    def display(self):
        i = 1
        for table in self.tables:
            print(f"\nTable {i}:")
            occupants = [seat.occupant for seat in table.seats]
            print(occupants)
            i += 1

    # store(filename) to store the repartition in an file
    def store(self, filename:str):
        with open(filename, "w", encoding="utf-8") as f:
            i = 1
            for table in self.tables:
                f.write(f"Table {i}: ")
                occupants = [seat.occupant if seat.occupant else "Free" for seat in table.seats]
                f.write(", ".join(occupants) + "\n")
                i += 1