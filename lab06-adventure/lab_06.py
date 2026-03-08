
class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west



if __name__ == "__main__":
    room_list = []
    room = Room("This is the starting room. There is a door to the north.", 1, None, None, None)
    room_list.append(room)
    room1 = Room(f"This is room 1. There is a door to the east, south and west.", None, 2, 2, 2)
    room_list.append(room1)
    room2 = Room(f"This is room 2. There is a door to the south.", None, None, 3, None)
    room_list.append(room2)
    room3 = Room(f"This is room 3. There is the final room.", None, None, None, None)
    room_list.append(room3)
    current_room = 0
    done = False
    while not done:
        print()
        print(room_list[current_room].description)
        i = input("What do you want to do? ")
        if (i == "n" or i == "N" or i == "North" or i == "NoRtH"):
            next_room = room_list[current_room].north
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif (i == "e" or i == "E" or i == "East" or i == "EaSt"):
            next_room = room_list[current_room].east
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif (i == "s" or i == "S" or i == "South" or i == "SoUtH"):
            next_room = room_list[current_room].south
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif (i == "w" or i == "W" or i == "West" or i == "WeSt"):
            next_room = room_list[current_room].west
            if next_room is None:
                print("You can't go that way.")
            else:
                current_room = next_room
        elif (i == "q" or i == "Q" or i == "Quit" or i == "QuIt"):
            print("Terminating the game.")
            done = True
        else:
            print("I don't understand what you typed.")