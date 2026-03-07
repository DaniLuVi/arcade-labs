
class Room:
    def __init__(self, description, north, east, south, west):
        self.description = description
        self.north = north
        self.east = east
        self.south = south
        self.west = west



def main():
    room_list = []
    room = Room("This is the starting room.", 1, None, None, None)
    for i in range(1, 5):
        room + str(i) = Room(f"This is room {i}.", None, None, None, None)
    room_list.append(room)
    current_room = 0