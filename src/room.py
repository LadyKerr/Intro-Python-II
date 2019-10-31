# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        n_to = None
        s_to = None
        e_to = None
        w_to = None
    
    def __str__(self):
        return f"\n Room name is: {self.name} and it is {self.description}. "
    
    def __repr__(self):
        return f"\n Room:({repr(self.name)}) Desc:({repr(self.description)}) "
    
    #add an item to room
    def add_item(self, room):
        self.rooms.append(room)