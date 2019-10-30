# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f"\n Player's name is: {self.name} and they are in room {self.current_room} right now. "
    
    def __repr__(self):
        return f"\n Player:({repr(self.name)}) Room:({repr(self.current_room)}) "